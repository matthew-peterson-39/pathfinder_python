import sys
import pygame
from queue import PriorityQueue, Queue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualizer")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
GREY = (128,128,128)
TURQUOISE = (64,224,208)
PURPLE = (128,0,128)

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
    
    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN
    
    def is_wall(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE
    
    def is_path(self):
        return self.color == BLUE

    def is_end(self):
        return self.color == YELLOW
    
    def reset(self):
        self.color = WHITE
    
    def make_path(self):
        self.color = BLUE

    def make_closed(self):
        self.color = RED
    
    def make_open(self):
        self.color = GREEN
    
    def make_wall(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE
    
    def make_end(self):
        self.color = YELLOW
    
    def draw(self, WIN):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.width))
    
    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row+1][self.col].is_wall(): # DOWN
            self.neighbors.append(grid[self.row+1][self.col])
        
        if self.row > 0 and not grid[self.row-1][self.col].is_wall(): # UP
            self.neighbors.append(grid[self.row-1][self.col])            
        
        if self.col < self.total_rows - 1 and not grid[self.row][self.col+1].is_wall(): # RIGHT
            self.neighbors.append(grid[self.row][self.col+1])
        
        if self.col > 0 and not grid[self.row][self.col-1].is_wall(): # LEFT
            self.neighbors.append(grid[self.row][self.col-1])

    # LESS THAN ... if two nodes are compared, the other spot will always be less than
    def __lt__(self, other):
        return False
    
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

def visualize_path(previous_node, current, draw):
    """
    Visualize the path from the start node to the current node.

    The previous_node dictionary is used to visualize the shortest path back
    to the start node. This is visualized through a color change and
    redrawing of the GUI with the draw() method after each path node is colored.
    
    Params:
    previous_node (dict): A dictionary storing the reference to the previous node for each visited.
    current (Node): The current node (first iteration is the end node) of the path to be visualized.
    draw (function): Helper function to update the GUI.
    """
    while current in previous_node:
        current = previous_node[current]
        current.make_path()
        draw()

def astar_algo(draw, grid, start, end):
    """
    A* search algorithm to find the shortest path from start to end node.
    
    This iterations of the A* algorithm uses a uniform-cost search, where each node's edges have the same weight.
    It makes use of a heuristic distance funct to compute optimal paths. The function maintains a priority queue of nodes to explore, along with 
    a 'g_score' representing the cost from the start node to the current node, and an 'f_score' 
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
        
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            # draw path
            visualize_path(previous_node, end, draw)
            end.make_end()
            return True

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
    print(start.y)
    print(end.y)
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

def make_grid(rows, width):
    grid = []
    gap = width // rows     #int division
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid

def draw_grid(WIN, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(WIN, GREY, (0,i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(WIN, GREY, (j * gap, 0), (j * gap, width)) #flip cords and draw vert borders

def draw(WIN, grid, rows, width):
    WIN.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(WIN)

    draw_grid(WIN, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y,x = pos

    row = y // gap
    col = x // gap

    return row, col

def main(WIN, width):
    algo_type = sys.argv[1] if len(sys.argv) > 1 else "astar" # default astar
    ROWS = 50
    grid = make_grid(ROWS, width)
    
    start = None
    end = None
    
    run = True
    started = False

    while run:
        draw(WIN, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:   #left mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node!= start:
                    end = node
                    end.make_end()
                elif node != end and node != start:
                    node.make_wall()
            
            elif pygame.mouse.get_pressed()[2]:   #right mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                node = grid[row][col]
                node.reset()

                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    if algo_type == "astar":
                        astar_algo(lambda: draw(WIN, grid, ROWS, width), grid, start, end)
                    elif algo_type == "dfs":
                        dfs_algo(lambda: draw(WIN, grid, ROWS, width), start, end)
                    elif algo_type == "bfs":
                        bfs_algo(lambda: draw(WIN, grid, ROWS, width), start, end)
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
    pygame.quit()

main(WIN, WIDTH)