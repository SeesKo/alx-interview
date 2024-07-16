#!/usr/bin/python3
"""
Script reads `stdin` line by line and computes metrics.
"""
import sys
import signal

# Initialize metrics
total_file_size = 0
status_code_counts = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """ Print the current statistics """
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")


def signal_handler(sig, frame):
    """ Handle the keyboard interrupt signal """
    print_stats()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read from standard input
for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) != 7:
            continue
        ip_address = parts[0]
        date = parts[2] + ' ' + parts[3]
        request = parts[4] + ' ' + parts[5] + ' ' + parts[6]
        status_code = int(parts[7])
        file_size = int(parts[8])

        # Update metrics
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

    except (ValueError, IndexError):
        # Ignore lines that don't have the expected format
        continue

# Print final stats if the script ends naturally
print_stats()
