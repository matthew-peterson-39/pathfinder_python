import pygame
from queue import PriorityQueue
from algorithms import utilities

"""
STUDY NOTES:
    - Initial thoughts: dijkstras algorithm seems to be an inbetween version of the A* and
    a BFS search. I do not fully understand what makes it different than a BFS, other than the
    edges having a cost associated with them, thus allowing a retracing back to the start via the
    shortest possible distance.

    - Final thoughts: Dijkstras algorithm at first looks very similar to A*. One big difference I noticed is that
    Dijkstra's algorithm works off of the g_score and does not account for the f_score function as is the case with 
    the A* algorithm. One can see that the additional f_score calculations leads to a more optimized seaarch.
"""

def dijkstras(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))  # count for breaking f-score ties
    
    previous_node = {}
    
    # set initial g_score for all nodes
    g_score = {node: float("inf") for row in grid for node in row}  #dictionary comprehension
    g_score[start] = 0

    open_set_hash = {start}     # faster open_set look up.

    while not open_set.empty():
        # Enables quit during runtime
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            utilities.visualize_path(previous_node, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                previous_node[neighbor] = current
                g_score[neighbor] = temp_g_score
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((temp_g_score, count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw()
        if current != start:
            current.make_closed()
    return False
        