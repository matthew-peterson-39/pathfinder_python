import pygame

def dfs_algo(draw, start, end):
    """
    Implements Depth First Search (DFS) to find a path from a start node to an end node.

    DFS explores as far down a branch as possible before backtracking. This version of DFS 
    goes to the end of a branch, then backtracks, checking other branches from the visited 
    nodes. It uses a stack to keep track of which nodes to visit next.

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
        # Enables quit during runtime
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = stack.pop()
        visited.add(current)

        if current == end:
            return True
        
        for neighbor in current.neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                if neighbor != end:
                    neighbor.make_open()

        draw()

        if current == end:
            return True
        if current != start:
            current.make_closed()

    return False