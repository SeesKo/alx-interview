#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys
import signal


def print_statistics(status_counts, total_file_size):
    """
    Print the current statistics.
    """
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")


def process_line(line, status_counts, total_file_size):
    """
    Process a single line of input.
    """
    parts = line.split()
    if (
        len(parts) == 7 and 
        parts[2] == '"GET' and 
        parts[3] == '/projects/260' and 
        parts[4] == 'HTTP/1.1"'
    ):
        try:
            status_code = parts[5]
            file_size = int(parts[6])
            total_file_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
        except ValueError:
            pass
    return total_file_size


def main():
    """
    Reads log lines, parses them to extract status codes
    and file sizes, and prints aggregated statistics.
    """
    status_counts = {
        str(code): 0 
        for code in [
            200, 301, 400, 401, 403, 404, 405, 500
        ]
    }
    total_file_size = 0
    line_count = 0

    def signal_handler(sig, frame):
        """
        Handles (Ctrl+C) signal to print statistics and exit program.
        """
        print_statistics(status_counts, total_file_size)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            total_file_size = process_line(line, status_counts, total_file_size)
            line_count += 1
            if line_count == 10:
                print_statistics(status_counts, total_file_size)
                line_count = 0
    finally:
        print_statistics(status_counts, total_file_size)


if __name__ == "__main__":
    main()
