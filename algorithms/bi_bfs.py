from queue import Queue

def bidirectional_bfs(draw, start, end):

    # initialize start and end locations
    start_queue = Queue()
    end_queue = Queue()
    visited_start = set([start])
    visited_end = set([end])

    while not start_queue.empty() and not end_queue.empty():
        current_start = start_queue.get()
        current_end = end_queue.get()

        # check if the paths have met
        if current_start == current_end or \
            current_start in visited_end or \
            current_end in visited_start:
            
            return True
            
        for neighbor in current_start.neighbors:
            if neighbor not in visited_start:
                visited_start.add(neighbor)
                start_queue.put(neighbor)
                neighbor.make_open()

        for neighbor in current_end.neighbors:
            if neighbor not in visited_end:
                visited_end.add(neighbor)
                end_queue.put(neighbor)
                neighbor.make_open()
        
        draw()
        
        if current_start != start:
            current_start.make_closed()
        if current_end != end:
            current_end.make_closed()

        