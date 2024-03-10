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

    coins.sort(reverse=True)

    num_coins = 0
    remaining_total = total

    for coin in coins:
        num_coin_used = remaining_total // coin
        remaining_total -= num_coin_used * coin
        num_coins += num_coin_used

        if remaining_total == 0:
            return num_coins

    return -1
