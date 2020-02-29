import gym
import time

env = gym.make('CartPole-v0')
env.reset()
for _ in range(500):
    env.render()
    observation, reward, done, info = env.step(env.action_space.sample())
    time.sleep(0.01)
env.close()
 