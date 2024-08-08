#!/usr/bin/python3
"""
    Defines a function called minOperations that computes minimum number of
    operations needed to arrive at a number of characters in file while been
    allowed only two operations(Copy All, Paste).
"""


def minOperations(n):
    """
        Returns the number of operations needed to arrive at a specific
        number of characters.
    """
    opts = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            opts += factor
            n //= factor
        factor += 1

    return opts
