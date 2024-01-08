"""
    1. First, initiate a stack with the starting vertex for the traversal.
    2. Pop from the stack and set this vertex as the “current” element or node.
    3. Now, find the neighboring vertexes (of the current node), and if they haven’t been visited push them into the stack.
    4. If no unvisited vertexes remain, go back and pop a vertex from the stack.
    5. Repeat steps 2, 3, and 4 until the stack is empty.
"""
def dfs_algo(draw, start, end):
    # intiate stack with start point
    stack = [start]
    #intial set for visited nodes
    visited = set()

    while stack:
        # get the first item in stack
        current = stack.pop()
        visited.add(current)

        if current == end:
            # Found the end node, perform necessary actions
            # like reconstructing the path and visualizing it.
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                stack.append(neighbor)

        draw()  # Redraw the grid with updated nodes

        if current != start:
            current.make_closed()  # Mark the current node as visited/closed in visualization

    return False
