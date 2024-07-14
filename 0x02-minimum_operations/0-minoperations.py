#!/usr/bin/python3
''' finding minimum operations '''


def minOperations(n):
    ''' function itself '''
    if n < 1 or not isinstance(n, int):
        return 0

    prime = [3, 5, 7, 2]

    if n in prime and n != 7:
        return n
    if n == 7:
        return 6

    for i in prime:
        if n % i == 0:
            k = n / i
            if k / 2 >= 5:
                z = minOperations(k)
                return int(z + i)
            else:
                return int(k + i)
