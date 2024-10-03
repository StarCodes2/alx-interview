#!/usr/bin/python3
""" Defines a function that finds the winner of a prime game. """


def isPrime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def findPrime(numList):
    """ finds the first prime number in a list. """
    count = 0
    for num in numList:
        if isPrime(num):
            return num
    return None


def isWinner(x, nums):
    """ Returns the winner of a prime game. """
    if x <= 0 or not nums:
        return None

    rounds = 1
    wins = [0, 0]
    for num in nums:
        if rounds > x:
            break

        rounds += 1
        numList = [i for i in range(1, num + 1)]
        pick = findPrime(numList)
        turn = 0

        while (pick):
            numList.remove(pick)

            mul = 2
            while pick * mul in numList:
                numList.remove(pick * mul)
                mul += 1

            pick = findPrime(numList)
            turn = 1 - turn

        if turn % 2 == 0:
            wins[1] += 1
        else:
            wins[0] += 1

    if wins[0] > wins[1]:
        return "Maria"
    elif wins[0] < wins[1]:
        return "Ben"
    else:
        return None
