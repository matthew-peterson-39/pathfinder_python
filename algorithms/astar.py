import pygame
from queue import PriorityQueue
from algorithms import utilities

def calculate_heuristic(node1, node2):
    """
    Method to calculate the Manhattan distance between two points. The Manhattan distance
    is represented by the absolute difference of Cartesian coordinates (x, y) between the
    two nodes. This approach restricts movement to the up, down, left, and right directions only.
    
    Params:
    node1 (tuple) - (x1, y1) cartesian coordinates of node1
    node2 (tuple) - (x2, y2) cartesian coordinates of node2
    
    Returns:
    int: Manhattan distance between node1 and node2.
    """
    x1, y1 = node1
    x2, y2 = node2

    return abs(x1 - x2) + abs(y1 - y2)

def astar_algo(draw, grid, start, end):
    """
    A* search algorithm to find the shortest path from start to end node.
    
    This iterations of the A* algorithm uses a uniform-cost search, where each node's edges have the same weight.
    It makes use of a heuristic distance funct to compute optimal paths. The function maintains a priority 
    queue of nodes to explore, along with a 'g_score' representing the cost from the start node to the current node, and an 'f_score' 
    that estimates the total cost from start to end going through the current node.

    Params:
    draw (function): Helper function to update the GUI.
    grid (list): 2D list representing the nodes in the grid.
    start (Node): The starting node of the path.
    end (Node): The ending node of the path.

    Returns:
    bool: True if a path is found, False otherwise.
    """
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))  # count for breaking f-score ties
    
    previous_node = {}
    
    # set initial g_score for all nodes
    g_score = {node: float("inf") for row in grid for node in row}  #dictionary comprehension
    g_score[start] = 0
    
    # set initial f_score for all nodes
    f_score = {node: float("inf") for row in grid for node in row}  #dictionary comprehension
    # calculate f_score using heuristic (manhattan distance) between the start and end node
    f_score[start] = calculate_heuristic(start.get_pos(), end.get_pos())

    open_set_hash = {start}     # faster open_set look up. 

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        current = open_set.get()[2] # Node obj
        open_set_hash.remove(current)

        if current == end:
            # draw path
            utilities.visualize_path(previous_node, end, draw)
            end.make_end()
            start.make_start()
            return True

        #get neighbors of current node
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                previous_node[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + calculate_heuristic(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        
        draw()
        
        if current != start:
            current.make_closed()
            
    return False