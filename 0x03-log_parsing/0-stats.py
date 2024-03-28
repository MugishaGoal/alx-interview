#!/usr/bin/env python3
"""A script that reads stdin line by line and computes metrics"""


import sys


def print_metrics(total_size, status_codes):
    '''Prints the computed metrics.'''
    print(f'Total file size: {total_size}')
    for code, count in sorted(status_codes.items()):
        print(f'{code}: {count}')


def parse_line(line):
    '''Parses the line and extracts IP Address, status code, and file size.'''
    parts = line.strip().split()
    if len(parts) < 9:
        return None, None, None
    ip_address = parts[0]
    status_code = parts[-2]
    file_size = parts[-1]
    if not status_code.isdigit():
        return None, None, None
    return ip_address, int(status_code), int(file_size)


def main():
    '''Main function to read stdin, compute metrics, and print statistics.'''
    total_size = 0
    status_codes = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0
            }
    try:
        for i, line in enumerate(sys.stdin, start=1):
            ip_address, code, file_size = parse_line(line)
            if ip_address is None:
                continue
            total_size += file_size
            if code in status_codes:
                status_codes[code] += 1
            if i % 10 == 0:
                print_metrics(total_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)


if __name__ == '__main__':
    main()
