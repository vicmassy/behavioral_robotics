import gym
import numpy as np
import time

env = gym.make('CartPole-v0')
# env = gym.make('Pendulum-v0')

episodes = 10
steps = 200
pvariance = 0.1 # variance of initial parameters
ppvariance = 0.02 # variance of perturbations
nhiddens = 5 # number of hidden neurons
ninputs = env.observation_space.shape[0]
if (isinstance(env.action_space, gym.spaces.box.Box)):
    noutputs = env.action_space.shape[0]
else:
    noutputs = env.action_space.n

def get_action(observation, W1, W2, b1, b2):
    # convert the observation array into a matrix with 1 column and ninputs rows
    observation.resize(ninputs,1)
    # compute the netinput of the first layer of neurons
    Z1 = np.dot(W1, observation) + b1
    # compute the activation of the first layer of neurons with the tanh function
    A1 = np.tanh(Z1)
    # compute the netinput of the second layer of neurons
    Z2 = np.dot(W2, A1) + b2
    # compute the activation of the second layer of neurons with the tanh function
    A2 = np.tanh(Z2)
    # if actions are discrete we select the action corresponding to the most activated unit
    if (isinstance(env.action_space, gym.spaces.box.Box)):
        action = A2
    else:
        action = np.argmax(A2)
    return action


def evaluate(W1, W2, b1, b2):
    fitness = 0
    for _ in range(episodes):
        #print("Starting episode %d", i)
        observation = env.reset()
        for _ in range(steps):
            # env.render()
            observation, reward, done, _ = env.step(get_action(observation, W1, W2, b1, b2))
            fitness += reward
            if done:
                #print("Finshed at iteration %d with fitness %d", j, fitness)
                break
    #env.close()
    return fitness


def train():
    lamda = 20 # population size (even number)
    g = 1000
    N = nhiddens*ninputs+noutputs*nhiddens+nhiddens+noutputs
    population = np.zeros((lamda, N)) # (lamda, (W1,W2,b1,b2))
    population[:, :-(nhiddens+noutputs)] = np.random.randn(lamda, N-nhiddens-noutputs)*pvariance
    nfitness = np.zeros(lamda)
    for gen in range(g):
        for i in range(lamda):
            p = population[i,:]
            W1 = p[:nhiddens*ninputs].reshape((nhiddens, ninputs))
            W2 = p[(nhiddens*ninputs):(N-nhiddens-noutputs)].reshape((noutputs, nhiddens))
            b1 = p[-(nhiddens+noutputs):-noutputs].reshape((nhiddens, 1))
            b2 = p[-noutputs:].reshape((noutputs, 1))
            nfitness[i] = evaluate(W1, W2, b1, b2)
        isorted = np.argsort(nfitness)
        print("Average fitness of generation " + str(gen+1) + " is "+str(nfitness.mean()) + " best: " + str(nfitness.max()))
        population = population[isorted, :]
        if nfitness.max()/episodes == steps:
            break
        population[:int(lamda/2), :] = population[int(lamda/2):, :]+np.random.randn(int(lamda/2), N)*ppvariance
    return population[-1, :]

p = train()
W1 = p[:nhiddens*ninputs].reshape((nhiddens, ninputs))
W2 = p[(nhiddens*ninputs):(nhiddens*ninputs+noutputs*nhiddens)].reshape((noutputs, nhiddens))
b1 = p[-(nhiddens+noutputs):-noutputs].reshape((nhiddens, 1))
b2 = p[-noutputs:].reshape((noutputs, 1))
for i in range(100):
    # print("Starting episode "+str(i))
    observation = env.reset()
    fitness = 0
    for j in range(steps):
        env.render()
        observation, reward, done, info = env.step(get_action(observation, W1, W2, b1, b2))
        fitness += reward
        if done:
            if fitness == steps:
                print("OK. Episode "+str(i+1)+" finshed with fitness "+str(fitness))
            else:
                print("FAIL. Episode "+str(i+1)+" finshed with fitness "+str(fitness))
            break
        #time.sleep(0.01)
env.close()