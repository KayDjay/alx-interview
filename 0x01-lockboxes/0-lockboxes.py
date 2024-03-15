#!/usr/bin/python3
""" model for Lockboxes """


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked given the provided configuration.

    Args:
        boxes: A list of lists where each element represents a box. Inner lists
               contain keys that can unlock other boxes.

    Returns:
        True if all boxes can be unlocked, False otherwise.
    """

    # Set of opened box indices
    seen = {0}
    # Queue of box indices to process
    queue = [0]

    while queue:
        # Get the next box to process
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            # Check if key is valid and new
            if key not in seen and key < len(boxes):
                # Mark the box as opened
                seen.add(key)
                # Add the box to the queue for further processing
                queue.append(key)

    # Check if all boxes have been opened
    return len(seen) == len(boxes)
