# hillclimb_8puzzle.py
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

def misplaced_tiles(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count

def print_state(state):
    for row in state:
        print(row)
    print("------")

def is_solvable(state):
    arr = [x for row in state for x in row if x != 0]
    inv = sum(1 for i in range(len(arr)) for j in range(i+1, len(arr)) if arr[i] > arr[j])
    return inv % 2 == 0

def hill_climbing(start_state):
    if not is_solvable(start_state):
        print("This puzzle is unsolvable.")
        return
    
    current = start_state
    while True:
        current_h = misplaced_tiles(current)
        neighbors = get_neighbors(current)
        if not neighbors:
            break
        
        best_neighbor = min(neighbors, key=misplaced_tiles)
        best_h = misplaced_tiles(best_neighbor)
        
        if best_h >= current_h:
            print("Local Optimum reached. Stopping.")
            print_state(current)
            return
        
        current = best_neighbor
        if current == goal_state:
            print("Goal Found using Hill Climbing!")
            print_state(current)
            return

if __name__ == "__main__":
    start = [[1, 2, 3],
             [4, 0, 6],
             [7, 5, 8]]
    hill_climbing(start)
