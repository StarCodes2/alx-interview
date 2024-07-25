#!/usr/bin/python3
""" Defines a function that generates the Pascal triangle """

def pascal_triangle(n):
    """ Generates a Pascal triangle depending on the value of n """
    triangle = []
    if n <= 0:
        return triangle

    for row in range(0, n):
        new = []
        if row < 1:
            new.append(1)
        else:
            tmp = 0
            for i, num in enumerate(triangle[len(triangle) - 1]):
                new.append(tmp + num)
                tmp = num
                if i == len(triangle) - 1:
                    new.append(num + 0)

        triangle.append(new)
    return triangle
