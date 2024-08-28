#!/usr/bin/python3
""" Defines the canUnlockAll function """


def canUnlockAll(boxes):
    """ Check boxes(list) for keys to other boxes. """
    unlocked = searchBox(boxes)
    print(unlocked)
    return len(unlocked) == len(boxes)


def searchBox(boxes, unlocked=set(), key=0):
    """ Traverse through a list using the keys in the list elements. """
    if key not in unlocked:
        unlocked.add(key)
    for nKey in boxes[key]:
        if nKey >= len(boxes):
            continue
        unlocked = searchBox(boxes, unlocked, nKey)

    return unlocked

