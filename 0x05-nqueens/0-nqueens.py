#!/usr/bin/python3
""" Solves the N queens problem using backtracking. """
import sys

if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

result = []


def noAttacks(board, row, col):
    """
        Check if a Queen can not attack and can not be attacked by other Queens
        if place in a cell.
    """
    for i in range(col):
        if board[row][i]:
            return False
    for i in range(row):
        if board[i][col]:
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while i >= 0 and j < len(board):
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True


def updateResult(board, length):
    """ Update the global result list with a solution. """
    points = []
    for row in range(length):
        for col in range(length):
            if board[row][col] == 1:
                points.append([row, col])
    result.append(points)


def findAll(board, row, length):
    """ Finds all possible solutions. """
    res = False
    for i in range(length):
        if noAttacks(board, row, i):
            board[row][i] = 1

            if row == length - 1:
                updateResult(board, length)
            else:
                findAll(board, row + 1, length)
            board[row][i] = 0


def solveNQueen(n):
    result.clear()
    board = [
        [0 for i in range(n)]
        for j in range(n)
    ]
    findAll(board, 0, len(board))
    for row in result:
        print(row)


solveNQueen(n)
