import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

import gym
env = gym.make("MountainCar-v0") #makes environment


TIME_LIMIT = 250
env = gym.wrappers.TimeLimit(gym.envs.classic_control.MountainCarEnv(),
                             max_episode_steps=TIME_LIMIT + 1)

s = env.reset()
actions = {'left': 0, 'stop': 1, 'right': 2}

# prepare "display"
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

def policy(t):
    # YOUR CODE HERE
    if s[1] >= 0: #position is s[0] | speed is s[1]
        return actions['right']
    elif s[1] < 0:
        return actions['left']

for t in range(TIME_LIMIT):
    s, r, done, _ = env.step(policy(t)) #s is observation, vector update. r is reward

    #draw game image on display
    ax.clear()
    ax.imshow(env.render('rgb_array'))
    fig.canvas.draw()

    if done:
        break

if done:
    print("Well done!")
else:
    print("Time limit exceeded. Try again.")
