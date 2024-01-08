import pygame
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

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
    #location of node
    #width of node
    #color of node
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
    
    def is_end(self):
        return self.color == TURQUOISE
    
    def reset(self):
        self.color == WHITE

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
        pass

    # LESS THAN ... if two nodes are compared, the other spot will always be less than
    def __let__(self, other):
        return False
    
def heuristic(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return abs(x1 - x2) + abs(y1 - y2)

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
            if start:   #ensure the user cannot press inputs when algorithm has started
                continue

            if pygame.mouse.get_pressed()[0]:   #left mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                node = grid[row][col]
                if not start:
                    start = node
                    start.make_start()
                elif not end:
                    end = node
                    end.make_end()
                elif node != end and node != start:
                    node.make_wall()
            
            elif pygame.mouse.get_pressed()[2]:   #right mouse button
                pass
    pygame.quit()

main(WIN, WIDTH)