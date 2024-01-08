import sys
import pygame
from queue import PriorityQueue
from algorithms import dfs, bfs, bi_bfs, bi_dfs, dijkstras, astar, utilities

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualizer")

BLACK = (96, 96, 96)
WHITE = (255, 255, 255)
RED = (255, 102, 102)
GREEN = (102, 255, 102)
BLUE = (102, 102, 255)
YELLOW = (255, 255, 102)
ORANGE = (255, 178, 102)
GREY = (160, 160, 160)
TURQUOISE = (102, 208, 204)
PURPLE = (204, 102, 255)

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
        return self.color == PURPLE
    
    def is_path(self):
        return self.color == BLUE

    def is_end(self):
        return self.color == ORANGE
    
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
                        astar.astar_algo(lambda: draw(WIN, grid, ROWS, width), grid, start, end)
                    elif algo_type == "dfs":
                        dfs.dfs_algo(lambda: draw(WIN, grid, ROWS, width), start, end)
                    elif algo_type == "bfs":
                        bfs.bfs_algo(lambda: draw(WIN, grid, ROWS, width), start, end)
                    elif algo_type == "bi_bfs":
                        bi_bfs.bidirectional_bfs(lambda: draw(WIN, grid, ROWS, width), start, end)
                    elif algo_type == "bi_dfs":
                        bi_dfs.bidirectional_dfs(lambda: draw(WIN, grid, ROWS, width), start, end)
                    elif algo_type == "dijkstras":
                        dijkstras.dijkstras(lambda: draw(WIN, grid, ROWS, width), grid, start, end)
                
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
    pygame.quit()

main(WIN, WIDTH)