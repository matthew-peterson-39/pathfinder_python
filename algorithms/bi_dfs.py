import pygame

def bidirectional_dfs(draw, start, end):
    start_stack = [start]
    start_visited = set()

    end_stack = [end]
    end_visited = set()
    

    while start_stack and end_stack:
        # Enables quit during runtime
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        start_current = start_stack.pop()
        start_visited.add(start_current)

        end_current = end_stack.pop()
        end_visited.add(end_current)

        if start_current == end_current or \
            start_current in end_stack or \
            end_current in start_stack:
            #TODO visualize path
            return True
        
        for neighbor in start_current.neighbors:
            if neighbor not in start_visited:
                start_stack.append(neighbor)
                if neighbor != end_current:
                    neighbor.make_open()
        
        for neighbor in end_current.neighbors:
            if neighbor not in end_visited:
                end_stack.append(neighbor) 
                if neighbor != start_current:
                    neighbor.make_open()

        draw()  # Redraw the grid with updated nodes

        if start_current != start:
            start_current.make_closed()
        
        if end_current != end:
            end_current.make_closed()

    return False