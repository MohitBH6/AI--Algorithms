# dfs_8puzzle.py
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

def to_tuple(s): 
    return tuple(tuple(r) for r in s)

def find_position(state, value):
    for i in range(3):
        for j in range(3):
            if state[i][j] == value:
                return i, j

def get_neighbors(state):
    x, y = find_position(state, 0)
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def print_state(state):
    for row in state:
        print(row)
    print("------")

def is_solvable(state):
    arr = [x for row in state for x in row if x != 0]
    inv = sum(1 for i in range(len(arr)) for j in range(i+1, len(arr)) if arr[i] > arr[j])
    return inv % 2 == 0

def dfs(start_state):
    if not is_solvable(start_state):
        print("This puzzle is unsolvable.")
        return
    
    stack = [start_state]
    visited = {to_tuple(start_state)}
    
    while stack:
        state = stack.pop()
        if state == goal_state:
            print("Goal Found using DFS!")
            print_state(state)
            return
        
        for nb in get_neighbors(state):
            t = to_tuple(nb)
            if t not in visited:
                visited.add(t)
                stack.append(nb)

if __name__ == "__main__":
    start = [[1, 2, 3],
             [4, 0, 6],
             [7, 5, 8]]
    dfs(start)
