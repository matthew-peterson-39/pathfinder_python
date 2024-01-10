import pygame
import random
import Line

pygame.init()

WIDTH, HEIGHT = 800, 800
GAP = 5
LINE_WIDTH = 10
NUM_LINES = 25
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.mouse.set_cursor(*pygame.cursors.arrow)
pygame.display.set_caption("Sorting Visualizer")

def create_lines(num_lines):
    lines_arr = []
    for i in range(num_lines):
        random_height = random.randint(1,100)
        height = (HEIGHT // 100) * random_height
        x = i * (LINE_WIDTH + GAP)
        y = HEIGHT - height
        line = Line.Line(x,y, LINE_WIDTH, height, color=(120,120,0))
        lines_arr.append(line)
    return lines_arr

# Draw array
def draw_array(arr):
    WIN.fill((0,0,0))  # Clear the screen
    for line in arr:
        line.draw(WIN)  # Draw each line
    pygame.display.flip()  # Update the display


def bubble_sort(arr):
    swapped = True
    lines = len(arr)
    while swapped:
        swapped = False
        for i in range(0, lines-1):
            arr[i].set_color((0,255,0))
            arr[i+1].set_color((0,255,0))
            
            if arr[i].height > arr[i+1].height:
                swapped = True
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                pygame.time.delay(50)
            draw_array(arr)

    if not swapped:
        pass


unsorted_lines = create_lines(NUM_LINES)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    WIN.fill((0,0,0))
    draw_array(unsorted_lines)
    bubble_sort(unsorted_lines)
    pygame.display.flip()

