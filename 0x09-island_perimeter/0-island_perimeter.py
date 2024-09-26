#!/usr/bin/python3
''' this module contain 0x09. Island Perimeter project'''


def island_perimeter(grid):
    ''' the function itself'''
    c = 0
    r = 0
    for i in grid:
        if 1 in i:
            c += 1
        for j in i:
            if j == 1:
                r += 1
    R = abs(r - c)
    R += 1
    return 2 * (c + R)
