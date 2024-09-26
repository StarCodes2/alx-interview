#!/usr/bin/python3
""" Calculates the perimeter of an island represented with a grid. """


def island_perimeter(grid):
    """ Returns the perimeter of a island represented by a list of lists. """
    perimeter = 0
    row = len(grid)
    for i in range(row):
        for j in range(len(grid[i])):
            col = len(grid[i])
            if grid[i][j] == 1:
                if i < 1 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i >= row or grid[i + 1][j] == 0:
                    perimeter += 1
                if j < 1 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j >= col or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
