#!/usr/bin/python3
"""
Method calculating fewest number of operations needed.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations required to
    make the number 'n' using copy and paste operations.
    """
    if n <= 1:
        return 0

    operations = 0
    d = 2
    while n > 1:
        while n % d == 0:
            operations += d
            n //= d
        d += 1

    return operations
