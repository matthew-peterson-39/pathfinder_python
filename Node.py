import pygame

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