#!/usr/bin/python3
import re
import sys
import signal

# Regular expression pattern to parse the log lines
log_pattern = re.compile(
        r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

# Dictionary to store the count of status codes
status_counts = {}
total_file_size = 0
line_count = 0

# List of valid status codes
valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}


def print_summary():
    """Print the current statistics."""
    print("File size: {}".format(total_file_size))
    for status in sorted(status_counts.keys()):
        print("{}: {}".format(status, status_counts[status]))


def signal_handler(sig, frame):
    """Handle the keyboard interruption signal (CTRL + C)."""
    print_summary()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def read_input():
    """Read input from stdin line by line."""
    global line_count, total_file_size
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            ip, date, status, size = match.groups()
            status = int(status)
            size = int(size)

            # Update the total file size
            total_file_size += size

            # Update the count for the status code
            if status in valid_status_codes:
                status_counts[status] = status_counts.get(status, 0) + 1

            # Increment the line count
            line_count += 1

            # Print the summary every 10 lines
            if line_count % 10 == 0:
                print_summary()


if __name__ == "__main__":
    read_input()
    print_summary()  # Ensure the summary is printed at the end
