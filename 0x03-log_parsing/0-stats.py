#!/usr/bin/python3
"""
Script reads `stdin` line by line and computes metrics.
"""
import sys
import signal

# Initialize the required variables
total_file_size = 0
status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Print the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C) and print statistics."""
    print_stats()
    sys.exit(0)


# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)


try:
    for line in sys.stdin:
        parts = line.split()
        # Ensure the log format is correct
        if len(parts) > 6 and parts[-2].isdigit() and parts[-1].isdigit():
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update the total file size
            total_file_size += file_size

            # Update the status code count if it's a valid code
            if status_code in status_codes:
                status_codes[status_code] += 1

            # Increment the line counter
            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_stats()
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)

# Print the final statistics
print_stats()
