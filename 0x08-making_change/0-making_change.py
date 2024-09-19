#!/usr/bin/python3
""" Defines that solves the change making problem. """


def makeChange(coins, total):
    """ Returns the minimum number of coins to make change
        a particular amount.
    """
    if total < 1:
        return 0
    mem = [float('inf')] * (total + 1)
    mem[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            mem[amount] = min(mem[amount], mem[amount - coin] + 1)

    return mem[total] if mem[total] != float('inf') else -1
