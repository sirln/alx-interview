#!/usr/bin/python3
'''
Module to calculate the perimeter of an island
'''


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    Args:
    grid (List[List[int]]): A list of lists of integers
    representing the grid where:
        0 represents water
        1 represents land

    Returns:
    int: The perimeter of the island.

    Example:
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    island_perimeter(grid)  # Output: 16
    """

    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
