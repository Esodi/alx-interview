#!/usr/bin/python3
"""
    pascal's triangle algorithm in python.
"""

def pascal_triangle(n):
    big = []
    if n <= 0:
        return big
    else:
        lst = [1]
        for j in range(n):
            lst1 = []
            x = 0
            y = 1
            lst1.append(1)
            for k in range(j):
                e = lst[x] + lst[y]
                lst1.append(e)
                x += 1
                y += 1
            lst1.append(1)
            big.append(lst)
            lst = lst1.copy()
    return big
