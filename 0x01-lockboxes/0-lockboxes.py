#!/usr/bin/python3
""" Defines the canUnlockAll function """


def canUnlockAll(boxes):
    """ Check boxes(list) for keys to other boxes. """
    keys = set()
    all_box = set()

    for key, box in enumerate(boxes):
        if key > 0:
            keys.add(key)
        if box and len(box) > 0:
            all_box.add(box[0])
    unlocked = keys & all_box

    return len(keys) == len(unlocked)
