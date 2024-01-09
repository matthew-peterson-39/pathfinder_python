import pygame
import random

pygame.init()
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.mouse.set_cursor(*pygame.cursors.arrow)
pygame.display.set_caption("Sorting Visualizer")

# generate a 50 element array of random values 1-100
arr = [random.randint(1, 100) for _ in range(50)]

# Draw array
def draw_array():
    pass

def bubble_sort():
    pass

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

