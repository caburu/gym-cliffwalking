from gym.envs.registration import register

register(
    id='cliffwalking-v0',
    entry_point='gym_cliffwalking.envs:CliffWalkingEnv',
)
