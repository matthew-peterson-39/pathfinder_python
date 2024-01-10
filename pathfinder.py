import sys
import pygame
import Node
from algorithms import dfs, bfs, bi_bfs, bi_dfs, dijkstras, astar

ROWS = 50
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.mouse.set_cursor(*pygame.cursors.arrow)
pygame.display.set_caption("Pathfinding & Search Algorithm Visualizer")

def initialize_grid(rows, width):
    grid = []
    gap = width // rows     #int division
    for x in range(rows):
        grid.append([])
        for y in range(rows):
            node = Node.Node(x, y, gap, rows)
            grid[x].append(node)
    return grid

def draw_node_borders(WIN, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(WIN, Node.GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(WIN, Node.GREY, (j * gap, 0), (j * gap, width)) #flip cords and draw vert borders

def draw_board(WIN, grid, rows, width):
    WIN.fill(Node.WHITE)
    for row in grid:
        for node in row:
            node.draw(WIN)
    draw_node_borders(WIN, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

def main(WIN, width):
    algo_type = sys.argv[1] if len(sys.argv) > 1 else "astar" # default astar
    grid = initialize_grid(ROWS, width)
    
    start = None
    end = None
    
    run = True
    started = False

    while run:
        draw_board(WIN, grid, ROWS, width)
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
                        astar.astar_algo(lambda: draw_board(WIN, grid, ROWS, width), grid, start, end)
                    elif algo_type == "dfs":
                        dfs.dfs_algo(lambda: draw_board(WIN, grid, ROWS, width), start, end)
                    elif algo_type == "bfs":
                        bfs.bfs_algo(lambda: draw_board(WIN, grid, ROWS, width), start, end)
                    elif algo_type == "bi_bfs":
                        bi_bfs.bidirectional_bfs(lambda: draw_board(WIN, grid, ROWS, width), start, end)
                    elif algo_type == "bi_dfs":
                        bi_dfs.bidirectional_dfs(lambda: draw_board(WIN, grid, ROWS, width), start, end)
                    elif algo_type == "dijkstras":
                        dijkstras.dijkstras(lambda: draw_board(WIN, grid, ROWS, width), grid, start, end)
                
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = initialize_grid(ROWS, width)
    pygame.quit()

main(WIN, WIDTH)