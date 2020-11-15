# gym-cliffwalking

An OpenAI Gym environment for Cliff Walking problem (from Sutton and Barto book).

## The Cliff Walking Environment

This environment is presented in the Sutton and Barto's book: Reinforcement Learning An Introduction (2 ed., 2018). The text and image below are from the book.

**Example 6.6: Cliff Walking** This gridworld example compares Sarsa and Q-learning, highlighting the difference between on-policy (Sarsa) and off-policy (Q-learning) methods. Consider the gridworld shown below. This is a standard undiscounted, episodic task, with start and goal states, and the usual actions causing movement up, down,right, and left. Reward is -1 on all transitions except those into the region marked “The Cliff”. Stepping into this region incurs a reward of -100 and sends the agent instantly back to the start.

![Cliff Walking representation](cliff_walking.png "Cliff Walking")

## This package

This minimalist package was created to be used as a [OpenAI Gym](https://gym.openai.com/) environment. The code was based on the exercises of [Reinforcement Learning Specialization](https://www.coursera.org/specializations/reinforcement-learning) from Coursera.

There is not a renderization of the environment (issue #1). Pull requests with this contribution are welcome.   :)

## Installation and Use

To install the package you need to clone (or download) the repository and use the command `pip install -e gym-cliffwalking`. 
To create an instance of the environment in python code use `gym.make('gym_cliffwalking:cliffwalking-v0')`.
