#!/usr/bin/python3
"""A method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    if len(boxes) == 0:
        return False

    visited = [False] * len(boxes)
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if 0 <= key < len(boxes) and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
