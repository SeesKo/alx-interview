#!/usr/bin/env python3
"""
Script that reads stdin line by line and computes metrics.
"""
import sys
import re

# Regular expression pattern to match the log format
LOG_PATTERN = (
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) '
    r'- \[(.*?)\] "GET /projects/260 HTTP/1\.1" '
    r'(\d{3}) (\d+)'
)

# HTTP status codes we are interested in
STATUS_CODES = ['200', '301', '400', '401', '403', '404', '405', '500']


def print_statistics(total_file_size, status_code_counts):
    """
    Print current statistics based on accumulated data.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if code in STATUS_CODES:
            print(f"{code}: {status_code_counts[code]}")


def main():
    """
    Reads log lines, parses them to extract status codes
    and file sizes, and prints aggregated statistics.
    """
    total_file_size = 0
    status_code_counts = {code: 0 for code in STATUS_CODES}
    line_counter = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.match(LOG_PATTERN, line)
            if match:
                status_code = match.group(3)
                file_size = int(match.group(4))

                total_file_size += file_size
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

                line_counter += 1

                if line_counter == 10:
                    print_statistics(total_file_size, status_code_counts)
                    line_counter = 0

    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print_statistics(total_file_size, status_code_counts)
        sys.exit(0)


if __name__ == "__main__":
    main()
