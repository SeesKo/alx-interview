#!/usr/bin/python3
"""
Determines the fewest number of coins needed.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins
    needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    # Early exit if any coin matches the total directly
    if total in coins:
        return 1

    # Initialize list to store the minimum coins needed for each amount
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    # Iterate through each coin and update the dp list
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[total] is still greater than total,
    # then it's not possible to make that amount
    return dp[total] if dp[total] <= total else -1
