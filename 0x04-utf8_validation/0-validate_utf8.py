#!/usr/bin/python3
"""
    Defnes a method that determines if a given data set represents a valid
    UTF-8 encoding.
"""


def validUTF8(data):
    """ Returns true if a data set represents a valid UTF-8 encoding and false
        otherwise.
    """
    num_bytes = 0
    check1 = 1 << 7
    check2 = 1 << 6

    for num in data:
        byte = num & 0xFF
        if num_bytes == 0:
            check = 1 << 7
            while check & byte:
                num_bytes += 1
                check >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & check1 and not (byte & check2)):
                return False
        num_bytes -= 1

    return num_bytes == 0
