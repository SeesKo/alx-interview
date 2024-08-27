#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in the grid.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Checking top
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Checking bottom
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Checking left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Checking right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
