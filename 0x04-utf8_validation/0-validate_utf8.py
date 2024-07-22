#!/usr/bin/python3
"""
Module contains a function to validate UTF-8 encoding.
"""


def validUTF8(data):
    """
    Checks if the given data set represents a valid UTF-8 encoding.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the significant bits in a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Loop through each integer in the data
    for num in data:
        # Get the binary representation of the integer
        bin_rep = format(num & 0xFF, '08b')

        # If this is the start of a new UTF-8 character
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            for bit in bin_rep:
                if bit == '0':
                    break
                num_bytes += 1

            # 1-byte characters (0xxxxxxx) have num_bytes set to 0
            if num_bytes == 0:
                continue

            # If the number of bytes is more than 4 or is 1, it's invalid
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # If this is not the first byte, it must start with '10'
            if not (num & mask1 and not (num & mask2)):
                return False

        # Decrement the number of bytes remaining in the UTF-8 character
        num_bytes -= 1

    # If we've processed all bytes and there's no pending bytes, it's valid
    return num_bytes == 0
