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
pat = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{1,7})\] "([A-Z]+) (/projects/\d+) HTTP/1\.1" (\d{3}) (\d+)'

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
            print('File size: {}'.format(s))
            for k, v in dct.items():
                if v > 0:
                    print(f'{k}: {v}')
            c = 0
            dct = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
