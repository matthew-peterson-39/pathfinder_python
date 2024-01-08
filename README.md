# Pathfinder Python
A pygame based pathfinding visualizer where users can design a maze and watch the algorithm work it out.

# Implemented Algorithms
- A-star (A*) - √

# Future Algorithms I want to Explore
- Bidirectional Search
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
WSL users may experience difficulties running the program depending on their version of Windows.
Vist https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps for additional details.

### Requirements
- Python 3
- Git
- Virtual Enviornmet (optional)

### Clone Repo
```bash
git clone https://github.com/matthew-peterson-39/pathfinder_python 
```

### Setup Virtual Envionrment

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

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run

```bash
python3 pathfinder.py
```

If the above run command returns an error try the following instead:
```bash
python pathfinder.py
```

