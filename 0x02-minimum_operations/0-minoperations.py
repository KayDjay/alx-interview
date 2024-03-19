#!/usr/bin/python3
""" This is Minimum OPerations Modules"""


def minOperations(n):
    """
    Calculate the minimum number of operations required to achieve a given
    number of characters.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations
