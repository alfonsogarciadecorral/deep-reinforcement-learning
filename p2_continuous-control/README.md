## Project Details

In this environment, a double-jointed arm can move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of your agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.

Number of agents: 1
Size of each action: 4
There are 1 agents. Each observes a state with length: 33

The environment is considered solved when score is >30 averaged over the last 100 episodes.

## Getting Started
Follow https://github.com/udacity/deep-reinforcement-learning#dependencies to install dependancies

## Instructions
Run Continuous_Control.ipynb