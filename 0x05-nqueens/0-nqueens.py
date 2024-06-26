#!/usr/bin/python3
""" N Queens Puzzles """

import sys


def is_safe(board, row, col):
    """ Checks if it's safe to place a queen at board[row][col].
    This function checks only left side for attacking queens. """
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N, board, col, solutions):
    """ Use backtracking to place queens in the board """
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(N, board, col + 1, solutions)
            board[i][col] = 0


def print_solutions(solutions):
    """ Prints the current board configuration as a list of lists containing
    the positions of the queens. """
    return [print(solution) for solution in solutions]


def main():
    # Checking the command line arguements
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize an empty chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Find and print all solutions
    solutions = []
    solve_nqueens(N, board, 0, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
