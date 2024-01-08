import pygame
from queue import PriorityQueue

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
        return self.color == TURQUOISE
    
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
        self.color = TURQUOISE
    
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
    while current in previous_node:
        current = previous_node[current]
        current.make_path()
        draw()

def astar_algo(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))  # count for breaking f-score ties
    previous_node = {}
    g_score = {node: float("inf") for row in grid for node in row}  #dictionary comprehension
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}  #dictionary comprehension
    f_score[start] = calculate_heuristic(start.get_pos(), end.get_pos())

    open_set_hash = {start}

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
            pygame.draw.line(WIN, GREY, (j * gap, 0), (j * gap, width)) #flip cords and draw ver

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
            # if start:   #ensure the user cannot press inputs when algorithm has started
            #     continue

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
                    astar_algo(lambda: draw(WIN, grid, ROWS, width), grid, start, end)
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
    pygame.quit()

main(WIN, WIDTH)