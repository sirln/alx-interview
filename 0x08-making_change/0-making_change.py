#!/usr/bin/python3
'''
Making change module
'''


def makeChange(coins, total):
    '''
    Calculate the fewest number of coins needed
    to meet a given amount total.

    Args:
        coins (list of int): List of coin values.
        total (int): Total amount to be met.

    Returns:
        int: Fewest number of coins needed to meet the total.
             Returns -1 if total cannot be met by any number of coins.
    '''
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
