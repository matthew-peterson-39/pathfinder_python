from queue import PriorityQueue

"""
STUDY NOTES:
    - Initial thoughts: dijkstras algorithm seems to be an inbetween version of the A* and
    a BFS search. I do not fully understand what makes it different than a BFS, other than the
    edges having a cost associated with them, thus allowing a retracing back to the start via the
    shortest possible distance.

    Reqs. 
"""

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

def dijkstras(draw, grid, start, end):
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
    pass