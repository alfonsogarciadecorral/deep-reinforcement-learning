import numpy as np
from collections import defaultdict
import random
class Agent:

    def __init__(self, nA=6, alpha=0.1, epsilon=0.1, gamma=0.9):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))   
        self.eps = epsilon
        self.alpha = alpha
        self.gamma = gamma

    def select_action(self, state):
        """Selects epsilon-greedy action for supplied state.
        
        Params
        ======
            Q (dictionary): action-value function
            state (int): current state
            nA (int): number actions in the environment
            eps (float): epsilon
        """
        if random.random() > self.eps: # select greedy action with probability epsilon
            return np.argmax(self.Q[state])
        else:                     # otherwise, select an action randomly
            return random.choice(np.arange(self.nA))

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        greedy_action = self.select_action(next_state)
        self.Q[state][action] += self.alpha*(reward +
                                             self.gamma*self.Q[next_state][greedy_action] -
                                             self.Q[state][action])