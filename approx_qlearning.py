import gym
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

env = gym.make("CartPole-v0").env
env.reset()
n_actions = env.action_space.n
state_dim = env.observation_space.shape
#position, angle, speed, angular speed
plt.imshow(env.render("rgb_array"))

import tensorflow as tf
import keras
import keras.layers as L
tf.reset_default_graph()
sess = tf.InteractiveSession()
keras.backend.set_session(sess)

network = keras.models.Sequential()
network.add(L.InputLayer(state_dim)) # state_dim is the dimensionality of a state (ie. 4).
                                     # INPUT LAYER w/ state_dim NUMBER OF INPUTS

# let's create a network for approximate q-learning following guidelines above
#<YOUR CODE: stack more layers!!! >

# create model
#network.add creates new layer
#Dense means neurons are all connected
network.add(L.Dense(100, activation='relu'))
                # ^the number of neurons
                                    # ^ see neural net notes for description. augments output of net
network.add(L.Dense(100, activation='relu'))
network.add(L.Dense(n_actions)) #OUTPUT LAYER. Trying to find actions in cartpole env. SO two outputs for two actions.

def get_action(state, epsilon=0):
    """
    sample actions with epsilon-greedy policy
    recap: with p = epsilon pick random action, else pick action with highest Q(s,a)
    """

    #network.predict is Keras' way of plugging into fx (ie. neural net)
    #passing some (?) number of states
    q_values = network.predict(state[None])[0]


    # number of actions
    possible_actions = n_actions

    #If there are no legal actions, return None
    if possible_actions == 0:
        return None

    if np.random.uniform() < epsilon:
        # choose random action
        chosen_action = np.random.choice(possible_actions)
    else:
        # choose best action from policy
        max_q = -np.Inf

        for a in range(possible_actions):
            this_q = q_values[a]
            if this_q > max_q:
                max_q = this_q
                chosen_action = a
    return chosen_action

#     return <epsilon-greedily selected action>

s = env.reset()
get_action(s)

# Create placeholders for the <s, a, r, s'> tuple and a special indicator for game end (is_done = True)
states_ph = keras.backend.placeholder(dtype='float32', shape=(None,) + state_dim)
#None means don't know how long episode is
actions_ph = keras.backend.placeholder(dtype='int32', shape=[None])
rewards_ph = keras.backend.placeholder(dtype='float32', shape=[None])
#concatinates tuple for each state ––> (state, state_dim)
next_states_ph = keras.backend.placeholder(dtype='float32', shape=(None,) + state_dim)
is_done_ph = keras.backend.placeholder(dtype='bool', shape=[None])

#get q-values for all actions in current states
#network is the name of the neural net fx
predicted_qvalues = network(states_ph) #for each state get out two values, dim = inputs : actions

#select q-values for chosen actions
predicted_qvalues_for_actions = tf.reduce_sum(predicted_qvalues * tf.one_hot(actions_ph, n_actions), axis=1)
#one-hot is a group of bits among which the legal combinations of values are only those with a single
#high (1) bit and all the others low (0).
#axis 1 = actions

gamma = 0.99

# compute q-values for all actions in next states
# <YOUR CODE - apply network to get q-values for next_states_ph>
predicted_next_qvalues = network(next_states_ph)

# compute V*(next_states) using predicted next q-values
# get max across actions axis (horizontal)
next_state_values = tf.reduce_max(predicted_next_qvalues, axis = 1)

# compute "target q-values" for loss - it's what's inside square parentheses in the above formula.
#!!!!!!!!!!!!
target_qvalues_for_actions = rewards_ph + gamma * next_state_values

# at the last state we shall use simplified formula: Q(s,a) = r(s,a) since s' doesn't exist

# if is_done_ph is true, return rewards, else return target_qvalues_for_actions
target_qvalues_for_actions = tf.where(is_done_ph, rewards_ph, target_qvalues_for_actions)

#mean squared error loss to minimize
#update predicted values by applying gradient descent ––> change weights for neural net
loss = (predicted_qvalues_for_actions - tf.stop_gradient(target_qvalues_for_actions)) ** 2
loss = tf.reduce_mean(loss) #***VALUE FOR SESSION***

# training function that resembles agent.update(state, action, reward, next_state) from tabular agent
train_step = tf.train.AdamOptimizer(1e-4).minimize(loss)

assert tf.gradients(loss, [predicted_qvalues_for_actions])[0] is not None, "make sure you update q-values for chosen actions and not just all actions"
assert tf.gradients(loss, [predicted_next_qvalues])[0] is None, "make sure you don't propagate gradient w.r.t. Q_(s',a')"
assert predicted_next_qvalues.shape.ndims == 2, "make sure you predicted q-values for all actions in next state"
assert next_state_values.shape.ndims == 1, "make sure you computed V(s') as maximum over just the actions axis and not all axes"
assert target_qvalues_for_actions.shape.ndims == 1, "there's something wrong with target q-values, they must be a vector"


def generate_session(t_max=1000, epsilon=0, train=False):
    """play env with approximate q-learning agent and train it at the same time"""
    total_reward = 0
    s = env.reset()

    for t in range(t_max):
        a = get_action(s, epsilon=epsilon)
        next_s, r, done, _ = env.step(a)

        if train:
            #run session using train_step w/ following inputs
            sess.run(train_step,{
                states_ph: [s], actions_ph: [a], rewards_ph: [r],
                next_states_ph: [next_s], is_done_ph: [done]
            })

        total_reward += r
        s = next_s
        if done: break

    return total_reward


epsilon = 0.5
for i in range(1000):
    session_rewards = [generate_session(epsilon=epsilon, train=True) for _ in range(100)]
    print("epoch #{}\tmean reward = {:.3f}\tepsilon = {:.3f}".format(i, np.mean(session_rewards), epsilon))

    epsilon *= 0.99
    assert epsilon >= 1e-4, "Make sure epsilon is always nonzero during training"

    if np.mean(session_rewards) > 300:
        print ("You Win!")
        break


#record sessions
import gym.wrappers
env = gym.wrappers.Monitor(gym.make("CartPole-v0"),directory="videos",force=True)
sessions = [generate_session(epsilon=0, train=False) for _ in range(100)]
env.close()

#show video
from IPython.display import HTML
import os

video_names = list(filter(lambda s:s.endswith(".mp4"),os.listdir("./videos/")))

HTML("""
<video width="640" height="480" controls>
  <source src="{}" type="video/mp4">
</video>
""".format("./videos/"+video_names[-1])) #this may or may not be _last_ video. Try other indices
