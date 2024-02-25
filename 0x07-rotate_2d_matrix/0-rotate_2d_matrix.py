#!/usr/bin/python3

"""
This module provides a function to rotate a given n x n 2D matrix
90 degrees clockwise in-place.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
    - matrix (list of lists): The input 2D matrix to be rotated.

    Returns:
    None. The matrix is edited in-place.

    Example:
    Given input matrix:
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

    After rotation, the matrix becomes:
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
    """

    n = len(matrix)

    # Transpose
    for i in range(n):
        for j in range(i, n):
            # Swap element at (i, j) with element at (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
