import gym
import numpy as np, pandas as pd

#500 states = 4 destinations * 5 passenger locations * 25 locations
env = gym.make("Taxi-v2")
env.reset() #resetting state of env. to known starting point
env.render()

policy = np.full((500,6), 1.0/n_actions) #makes a 500 by 6 array filled with a constant it. 1/n_actions

# 1 game with max limit of 100000 time steps
def generate_session(policy, t_max=10**4):

    states, actions = [],[] #way of recording states and actions
    total_reward = 0.

    s = env.reset()

    for t in range(t_max):
        policy_state = policy[s, :] #from policy –> the table (ie. contains the distibutions)
                                    #from state pick the whole row (actions)

        #np.random choice picks action based off of distribution
        a = int(np.random.choice(n_actions, 1, p = policy_state)) # range of actions through n_actions (6)|
                                                                  # "1" answer | distribution(p) = policy_state

        new_s, r, done, info = env.step(a) #new state, reward, game over?, info

        #Record state, action and add up reward to states, actions and total_reward accordingly.
        states.append(s)
        actions.append(a)
        total_reward += r # cumulative sum

        s = new_s
        if done:
            break
    return states, actions, total_reward #returns one game

def select_elites(states_batch,actions_batch,rewards_batch,percentile=50):

    #<Compute minimum reward for elite sessions. Hint: use np.percentile>
    # gets 50th percentile reward form batch
    reward_threshold = np.percentile(rewards_batch, percentile)
    elite_states  = []
    elite_actions = []


    for i in range(len(rewards_batch)): #for each value in rewards batch (reward total of each game)
        if rewards_batch[i] >= reward_threshold: #check to see if value is greater than threshold (based off of percentile)
            for j in range(len(states_batch[i])): #for each value in states batch (states in each game)
                elite_states.append(states_batch[i][j]) #append each state for the game to elite_states
                elite_actions.append(actions_batch[i][j]) #^^^

    print( elite_states, elite_actions)
    return elite_states, elite_actions #return states and actions that yielded good rewards

def update_policy(elite_states,elite_actions):

    new_policy = np.zeros([n_states,n_actions])

    #<Your code here: update probabilities for actions given elite states & actions>
    #Don't forget to set 1/n_actions for all actions in unvisited states.

    for i in range(len(new_policy)): #for each state in new_policy
        num_updates = 0 #keeps track of times we update each state
        for j in range(len(elite_states)): # for each state
            if i == elite_states[j]: # if the state of the policy == elite state
                num_updates +=1 #update
                action = elite_actions[j] #get the action
                new_policy[i][action] += 1 #set the probability of that action = 1
        if num_updates == 0:
            new_policy[i] = 1.0 / n_actions #if no updates set distribution to avg 1/6
        else:
            new_policy[i] /= num_updates # divide by the number of updates to get valid probability distribution
    return new_policy

from IPython.display import clear_output

def show_progress(batch_rewards, log, percentile, reward_range=[-990,+10]):

    # gets avg reward / reward threshold
    mean_reward, threshold = np.mean(batch_rewards), np.percentile(batch_rewards, percentile)
    log.append([mean_reward,threshold])

    clear_output(True)
    print("mean reward = %.3f, threshold=%.3f"%(mean_reward, threshold))
    plt.figure(figsize=[8,4])
    plt.subplot(1,2,1) #multiple plots in one plot... rows, columns, actual pos
    plt.plot(list(zip(*log))[0], label='Mean rewards') #make separate list Mean reward and plot
    plt.plot(list(zip(*log))[1], label='Reward thresholds')#make separate list reward threshold and plot
    plt.legend()
    plt.grid()

    plt.subplot(1,2,2)
    plt.hist(batch_rewards,range=reward_range);
    plt.vlines([np.percentile(batch_rewards, percentile)], [0], [100], label="percentile", color='red')
    plt.legend()
    plt.grid()

    plt.show()

def run_program(policy):
    n_sessions = 250  #sample this many sessions
    percentile = 50  #take this percent of session with highest rewards
    learning_rate = 0.3  #add this thing to all counts for stability

    log = []

    for i in range(100):

        sessions = [generate_session(policy) for x in range(n_sessions)] #runs n_session states and sets = to sessions
        batch_states, batch_actions, batch_rewards = zip(*sessions) #unzips returned session into three lists

        elite_states, elite_actions = select_elites(batch_states, batch_actions, batch_rewards)

        new_policy = update_policy(elite_states, elite_actions)

        #averaging old and new policy w/learning rate... rely on old knowledge so don't ignore new states
        policy = learning_rate * new_policy + (1-learning_rate) * policy

        #display results on chart
        show_progress(batch_rewards, log, percentile)
    return policy
