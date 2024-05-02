#!/usr/bin/python3
"""Change comes from within Module"""


def makeChange(coins, total):
    """
    Calculates minimum number of coins needed to make change to arrive total

    Args:
        coins (list): A list of coin denominations available.
        total (int): The total amount for which change needs to be made.

    Returns:
        int: Minimum number of coins needed to make change to arrives total.
             Returns -1 if it is not possible to make change for given total

    """
    if total <= 0:
        return 0
    if total > 0 and len(coins) == 0:
        return -1

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(1, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
