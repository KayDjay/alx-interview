def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked given the provided key configuration.

    Args:
        boxes: A list of lists where each element represents a box. Inner lists 
               contain keys that can unlock other boxes.

    Returns:
        True if all boxes can be unlocked, False otherwise.
    """

    seen = {0}  # Set of opened box indices
    queue = [0]  # Queue of box indices to process

    while queue:
        current_box = queue.pop(0)  # Get the next box to process
        for key in boxes[current_box]:
            if key not in seen and key < len(boxes):  # Check if key is valid and new
                seen.add(key)  # Mark the box as opened
                queue.append(key)  # Add the box to the queue for further processing

    return len(seen) == len(boxes)  # Check if all boxes have been opened