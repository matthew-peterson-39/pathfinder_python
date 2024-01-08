"""
BFS WIKIPEDIA PSUEDOCODE:
1  procedure BFS(G, root) is
2      let Q be a queue
3      label root as explored
4      Q.enqueue(root)
5      while Q is not empty do
6          v := Q.dequeue()
7          if v is the goal then
8              return v
9          for all edges from v to w in G.adjacentEdges(v) do
10              if w is not labeled as explored then
11                  label w as explored
12                  w.parent := v
13                  Q.enqueue(w)
"""
from queue import Queue

def bfs_algo(draw, start, end):
    queue = Queue()
    visited = set()

    queue.put(start)
    visited.add(start)

    while not queue.empty():
        current = queue.get()
        if current == end:
            return True
        
        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put(neighbor)
                neighbor.previous_node = current
            
        draw()

        if current != start:
            current.make_closed()
    
    return False