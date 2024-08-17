#!/usr/bin/python3

import sys
import re
from collections import defaultdict

def process_line(line):
    # Regular expression for parsing the log line
    regex = r'^(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "GET /projects/\d+ HTTP/1\.1" (\d{3}) (\d+)$'
    match = re.match(regex, line)
    if match:
        ip_address, date, status_code, file_size = match.groups()
        return int(status_code), int(file_size)
    return None, None

def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            status_code, file_size = process_line(line)
            if status_code and file_size is not None:
                total_size += file_size
                status_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_size, status_counts)
                    
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()

