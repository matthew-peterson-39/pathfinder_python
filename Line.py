import pygame

class Line:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width  
        self.height =  height   # Uses the array values from sorting.py
        self.color = color
    
    def set_color(self, new_color):
        self.color = new_color

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def update_height(self, new_height):
        pass