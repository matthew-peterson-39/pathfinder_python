import pygame

class Line:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height =  height
        self.color = color
    
    def draw(self, window):
        pass

    def update_height(self, new_height):
        pass

    def change_color(self, new_color):
        pass