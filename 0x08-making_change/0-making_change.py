#!/usr/bin/python3
"""Change comes from within Module"""


def makeChange(coins, total):
    """
    Calculates the minimum number of coins needed to make change for a given total.

    Args:
        coins (list): A list of coin denominations available.
        total (int): The total amount for which change needs to be made.

    Returns:
        int: The minimum number of coins needed to make change for the given total.
             Returns -1 if it is not possible to make change for the given total.

    """
    if total <= 0:
        return 0
    if total > 0 and len(coins) == 0:
        return -1
    
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
