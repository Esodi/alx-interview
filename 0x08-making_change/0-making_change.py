#!/usr/bin/python3
''' making change '''


def makeChange(coins, total):
    '''making change'''
    if total <= 0:
        return 0
    dp = [total + 1] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    return dp[total] if dp[total] != total + 1 else -1
