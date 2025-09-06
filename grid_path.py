# grid_path.py
from collections import deque

def shortest_path(grid, start, goal):
    """
    grid: list of lists, 0 = free, 1 = blocked
    start, goal: (r,c)
    """
    R = len(grid); C = len(grid[0])
    q = deque([(start, [start])])
    seen = {start}
    while q:
        (r,c), path = q.popleft()
        if (r,c) == goal:
            return path
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc]==0:
                if (nr,nc) not in seen:
                    seen.add((nr,nc))
                    q.append(((nr,nc), path+[(nr,nc)]))
    return None

if __name__ == "__main__":
    grid = [
        [0,0,0,0],
        [1,1,0,1],
        [0,0,0,0],
        [0,1,1,0]
    ]
    start=(0,0); goal=(3,3)
    p = shortest_path(grid, start, goal)
    print("Path:", p)
