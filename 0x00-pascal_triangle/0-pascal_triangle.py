#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [None for _ in range(i + 1)]
        row[0], row[-1] = 1, 1  # First and last element of each row is 1

        # Fill the row except the first and last element
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
