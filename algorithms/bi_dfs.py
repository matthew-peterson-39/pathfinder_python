def bidirectional_dfs(draw, start, end):
    """
    Implements a bidirectional Depth First Search (Bi-DFS) to find a path from a start node to an end node concurrently.
    
    Params:
    draw (function): Function to update the GUI.
    start (Node): The starting point of the search.
    end (Node): The target node to find.

    Returns:
        bool: True if a path to the end node is found, False if there's no path.
    """
   
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()
        visited.add(current)

        if current == end:
            #TODO visualize path
            return True
        
        for neighbor in current.neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                if neighbor != end:
                    neighbor.make_open()

        draw()  # Redraw the grid with updated nodes

        if current != start:
            current.make_closed()  # Mark the current node as visited/closed in visualization

    return False