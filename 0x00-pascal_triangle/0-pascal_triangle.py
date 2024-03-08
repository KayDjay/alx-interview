#!/usr/bin/python3
"""Pascal's Triangle"""

def pascal_triangle(n):
    """Returns the pascal triangle for the given number.

    Args:
        n (int): The number for which the pascal's triangle is to be generated.

    Returns:
        list: The pascal triangle for the given number.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
