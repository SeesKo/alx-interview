#!/usr/bin/python3
"""
Rotates a 2D matrix by 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates the matrix in place by 90 degrees clockwise.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
