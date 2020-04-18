from gym.envs.registration import register
register(
    id='BalanceBotBulletEnv-v0',
    entry_point='balance_bot.envs:BalancebotEnv',
)