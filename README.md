# Pathfinding with Python
A pygame based pathfinding visualizer where users can design a maze and watch the algorithm work it out. The current version works on an unweighted graph, where all node edges have the same value. In the future, I want to implement different weights for more maze building options.

# Implemented Algorithms
- A*
- DFS
- BFS
- Bidirectional BFS
- Bidirectional DFS
- Dijkstra's Algorithm

# Future Algorithms I want to Explore
- Swarm Algorithm

# Controls
### Left-click: 
>Place start, end, or wall.
### Right-click: 
>Reset node at mouse position.

### Keypress C:
>Reset entire grid.
### Keypress SPACE:
>Start search.

# How to Run

## NOTICE:
WSL users who's version of windows is < X11 may experience difficulties running the program.
Vist https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps for additional details.

## Requirements
- Python 3
- Git
- Virtual Enviornmet (optional)

## Clone Repo
```bash
git clone https://github.com/matthew-peterson-39/pathfinder_python 
```

## Setup Virtual Envionrment

Change directories into cloned repo
```bash 
cd pathfinder_python
```

Create virtual enviornment
```bash 
python -m venv .venv
```

Activate virtual enviornment

Mac :
```bash
source .venv/bin/activate
```

Windows :
```bash
source .venv/Scripts/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run

### algo_type Options:

1. astar
2. dfs
3. bfs
4. bi_bfs
5. bi_dfs
6. dijkstras

```bash
python3 pathfinder.py <algo_type>
```

If the above run command returns an error try the following instead:
```bash
python pathfinder.py <algo_type>
```

