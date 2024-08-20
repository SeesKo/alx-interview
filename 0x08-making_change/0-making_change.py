#!/usr/bin/python3
"""
Determines the fewest number of coins needed.
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins
    needed to meet the total amount.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for the greedy approach
    coins = sorted(coins, reverse=True)
    count = 0

    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            count += total // coin
            total %= coin

    return count if total == 0 else -1
