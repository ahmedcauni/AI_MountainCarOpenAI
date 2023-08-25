

import gym
import numpy as np

env = gym.make("MountainCar-v0")
print(env.observation_space.high)
print(env.observation_space.low)
print(env.action_space.n)

env.reset()
action=env.action_space.sample()
nouse,reward,done,info=env.step(action)
print(nouse,reward,done)

#Random Strategy
EPISODES = 4000
done=False
episode_reward = 0
env.reset()
won =0
for i in range (EPISODES):
    if done:
        if episode_reward <-200:
            won+=1
        print(episode_reward)
        env.reset()
        episode_reward = 0
        done=False
    else :
        for y in range (200):
            action=env.action_space.sample()
            nouse,reward,done,info=env.step(action)
            episode_reward+=reward

print ("won :" , won , "times")


#Qlearning Strategy 
DState= [20] * 2 
DSG = (env.observation_space.high - env.observation_space.low)/DState
Q_intial = np.random.uniform(low=-2, high=0, size=(DState + [env.action_space.n]))


def makedisc(state):
    d_state = (state - env.observation_space.low)/DSG
    return tuple(d_state.astype(np.int))

EPISODES = 4000
Gamma = 0.95
LEARNING_RATE = 0.1
Show = 1000
epsilon = 1
START_EPSILON_DECAYING = 1
END_EPSILON_DECAYING = EPISODES//2
epsilon_decay_value = epsilon/(END_EPSILON_DECAYING - START_EPSILON_DECAYING)



for episode in range(EPISODES):
    if episode_reward >-200:
            won+=1
    episode_reward = 0
    d_state = makedisc(env.reset())
    done = False
    while not done:
        if np.random.random() > epsilon:
            
            action = np.argmax(Q_intial[d_state])
        else:
            
            action = np.random.randint(0, env.action_space.n)

        new_state, reward, done, info = env.step(action)
        episode_reward += reward
        new_d_state = makedisc(new_state)


        if not done:

           
            max_q = np.max(Q_intial[new_d_state])

            
            current_q = Q_intial[d_state + (action,)]

           
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + Gamma * max_q)

            
            Q_intial[d_state + (action,)] = new_q


       
        elif new_state[0] >= env.goal_position:
            Q_intial[d_state + (action,)] = 0

        d_state = new_d_state
    print(episode_reward)
  
    if END_EPSILON_DECAYING >= episode >= START_EPSILON_DECAYING:
        epsilon -= epsilon_decay_value


print ("won :" , won , "times")

