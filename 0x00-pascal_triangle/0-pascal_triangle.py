#!/usr/bin/python3
'''
Pascal's Triangle
'''

def pascal_triangle(n):
    triangle = []

    if n <= 0:
        return triangle

    triangle = [[1]]

    for l in range(1, n):
        row = [1]

        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip (last_row, last_row[1:])])

        row.append(1)
        triangle.append(row)

    return triangle
