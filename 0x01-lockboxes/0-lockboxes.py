def canUnlockAll(boxes):
    # Create a set to keep track of the keys we have
    keys = set([0])

    # Create a set to keep track of the boxes we have visited
    visited = set()

    # Start with the first box
    stack = [0]

    # Iterate through the stack until it's empty
    while stack:
        # Pop the top box from the stack
        box = stack.pop()

        # Mark the box as visited
        visited.add(box)

        # Check if we have the key to open the box
        if box in keys:
            # Add the keys in the box to our set of keys
            keys.update(boxes[box])

            # Add the unvisited boxes to the stack
            stack.extend(set(boxes[box]) - visited)

    # Check if we have visited all the boxes
    return len(visited) == len(boxes)
