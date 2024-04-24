#!/usr/bin/python3
""" This Rotate 2D Matrix modules"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix in-place by 90 degrees clockwise.

    Args:
        matrix (list[list]): The 2D matrix to be rotated.

    Returns:
        None: The function modifies the input matrix in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row of the transposed matrix
    for i in range(n):
        matrix[i].reverse()
