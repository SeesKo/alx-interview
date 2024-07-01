#!/usr/bin/python3
"""
Method determining if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    """
    if not boxes:
        return False

    n = len(boxes)
    opened = set()
    stack = [0]  # Start with the first box

    while stack:
        box = stack.pop()
        if box not in opened:
            opened.add(box)
            for key in boxes[box]:
                if key < n and key not in opened:
                    stack.append(key)

    return len(opened) == n
