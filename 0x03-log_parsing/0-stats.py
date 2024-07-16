#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""
import sys
import re
from collections import defaultdict


def parse_log_line(line):
    """
    Parse a log line and extract IP, status code, and file size.
    """
    pattern = (
        r'^\s*(\d+\.\d+\.\d+\.\d+)\s+-\s+\[(.*?)\]\s+"GET /projects/260 '
        r'HTTP/1\.1"\s+(\d+)\s+(\d+)\s*$'
    )
    match = re.match(pattern, line)
    if match:
        status_code = match.group(3)
        file_size = int(match.group(4))
        return (status_code, file_size)
    return None


def print_statistics(total_file_size, status_code_counts):
    """
    Print the current statistics.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")
    print()


def main():
    """
    Reads log lines, parses them to extract status codes
    and file sizes, and prints aggregated statistics.
    """
    total_file_size = 0
    status_code_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parsed_data = parse_log_line(line)
            if parsed_data:
                status_code, file_size = parsed_data
                total_file_size += file_size
                status_code_counts[status_code] += 1
                line_count += 1

                if line_count == 10:
                    print_statistics(total_file_size, status_code_counts)
                    line_count = 0

    except KeyboardInterrupt:
        pass  # Catch Ctrl+C to exit gracefully

    finally:
        print_statistics(total_file_size, status_code_counts)


if __name__ == "__main__":
    main()
