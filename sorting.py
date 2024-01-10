import pygame
import random
import Line

pygame.init()
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_cursor(*pygame.cursors.arrow)
pygame.display.set_caption("Sorting Visualizer")

# generate a 50 element array of random values 1-100
arr = [random.randint(1, 100) for _ in range(50)]

# Draw array
def draw_array():
    width = 10
    gap = 5
    for i, j in enumerate(arr):
        height = (HEIGHT / 100) * j
        x = (width + gap) * i
        y = HEIGHT - height 
        line = Line.Line(x, y, width, height, color=(120,120,0))
        line.draw(WIN)

def bubble_sort(arr):
    sorted = []
    lines = len(arr)
    for i in range(lines):
        swapped = False
        for j in range(0, lines-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
    
    if not swapped:
        pass


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    WIN.fill((0,0,0))
    draw_array()
    bubble_sort(arr)
    pygame.display.flip()

