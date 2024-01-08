def visualize_path(previous_node, current, draw):
    """
    Visualize the path from the start node to the current node.

    The previous_node dictionary is used to visualize the shortest path back
    to the start node. This is visualized through a color change and
    redrawing of the GUI with the draw() method after each path node is colored.
    
    Params:
    previous_node (dict): A dictionary storing the reference to the previous node for each visited.
    current (Node): The current node (first iteration is the end node) of the path to be visualized.
    draw (function): Helper function to update the GUI.
    """
    while current in previous_node:
        current = previous_node[current]
        current.make_path()
        draw()