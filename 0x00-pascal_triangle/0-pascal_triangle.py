#!/usr/bin/python3
"""
Code defines a function that returns a list of lists of integers that represents the Pascal's triangle of y
"""


def pascal_triangle(n):
    """
    parameters that will be used:
    y [int]: Pascal triangle rows that will be created

    to return:
        [list of lists of integers]: this represents the Pascal's triangle
    """
    if type(y) is not int:
        raise TypeError("y is an integer")
    triangle = []
    if y <= 0:
        return triangle
    previous = [1]
    for row_index in range(y):
        rowlist = []
        if row_index == 0:
            rowlist = [1]
        else:
            for i in range(row_index + 1):
                if i == 0:
                    rowlist.append(0 + previous[i])
                elif i == (row_index):
                    rowlist.append(previous[i - 1] + 0)
                else:
                    rowlist.append(previous[i - 1] + previous[i])
        previous = rowlist
        triangle.append(rowlist)
    return triangle
