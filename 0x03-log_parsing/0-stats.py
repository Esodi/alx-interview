#!/usr/bin/python3
'''
Script that reads stdin line by line and computes metrics.
'''

import sys
import signal
import re

def exiting(sig, frame):
    '''Handle SIGINT (Ctrl+C) to print results before exiting.'''
    for k, v in dct.items():
        if v > 0:
            print(f'{k}: {v}')
    print(f'File size: {s}')
    sys.exit(0)

signal.signal(signal.SIGINT, exiting)

c, s = 0, 0
dct = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
pat = re.compile(
    r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+ - \[([0-9]+-[0-9]+-[0-9]+\s[0-9]+:[0-9]+:[0-9]+\.[0-9]+)\] "GET /projects/260 HTTP/1.1" ([0-9]+) ([0-9]+)'
)

for line in sys.stdin:
    line = line.strip()
    match = pat.match(line)
    if match:
        status_code = int(match.group(2))
        file_size = int(match.group(3))
        s += file_size
        if status_code in dct:
            dct[status_code] += 1
        c += 1
        if c % 10 == 0:
            for k, v in dct.items():
                if v > 0:
                    print(f'{k}: {v}')
            print(f'File size: {s}')
            # Note: Resetting the counters for the next batch of 10 lines
            dct = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
            s = 0

