#!/usr/bin/python3
'''
 script that reads stdin line by line and computes metrics
'''

import os
import sys
import signal
import re


def exiting(sig, frame):
    ''' func for ctrl + c '''
    for k, v in dct.items():
        if v > 0:
            print(f'{k}: {v}')
    print('File size: {}'.format(s))
    sys.exit(0)


signal.signal(signal.SIGINT, exiting)


c, s = 0, 0
nlst = []
dct = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
pat = r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+ - \[([0-9]+-[0-9]+-[0-9]+\s[0-9]+:[0-9]+:[0-9]+\.[0-9]+)\] "GET /projects/260 HTTP/1.1" [0-9]+ [0-9]+'
for i in sys.stdin:
    line = i.strip()
    if re.match(pat, line):
        lst = line.split(' ')
        s += int(lst[-1])
        code = int(lst[-2])
        nlst.append(code)
        if code in dct:
            v = int(dct[code]) + 1
            dct[code] = v
        c += 1
        if c == 10:
            for k, v in dct.items():
                if v > 0:
                    print(f'{k}: {v}')
            print('File size: {}'.format(s))
            c = 0
            s = 0
            dct = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
