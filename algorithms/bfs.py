from queue import Queue
import pygame

def bfs_algo(draw, start, end):
    """
    Implements the Breadth First Search (BFS) algorithm to find a path from a start 
    node to an end node.

    BFS works level by level, first checking all neighbors of the start node, then moving
      to the next level of neighbors if the end node isn't found. It uses a queue to keep 
      track of which nodes to visit next. The function ends when it either finds the end 
      node or runs out of nodes to check.

    Params:
    draw (function): Function to update the GUI.
    start (Node): The starting point of the search.
    end (Node): The target node to find.

    Returns:
    bool: True if a path to the end node is found, False if there's no path.
    """
    queue = Queue()
    visited = set()

    queue.put(start)
    visited.add(start)

    while not queue.empty():
        # Enables quit during runtime
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = queue.get()
        if current == end:
            #TODO visualize path
            return True
        
        for neighbor in current.neighbors:
            if neighbor not in visited:
                if neighbor != end:
                    neighbor.make_open()
                visited.add(neighbor)
                queue.put(neighbor)
                neighbor.previous_node = current
            
        draw()

        if current != start:
            current.make_closed()
    
    return False