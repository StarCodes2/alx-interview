#!/usr/bin/python3
""" Defines that solves the change making problem. """


def makeChange(coins, total):
    """ Returns the minimum number of coins to make change
        a particular amount.
    """
    if total < 1:
        return 0
    mem = [total + 1 for i in range(total + 1)]

    for idx, val in enumerate(mem):
        if idx == 0:
            mem[idx] = 0
        for coin in coins:
            remain = idx - coin
            if remain >= 0:
                mem[idx] = min(mem[remain] + 1, mem[idx])
    return -1 if mem[total] > total else mem[total]
