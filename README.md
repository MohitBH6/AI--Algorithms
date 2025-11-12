🎯 Aim

To implement and analyze different search techniques (DFS, BFS, Hill Climbing, and Heuristic (A) Search*) for solving the 8 Puzzle Problem.

🧠 Problem Description

The 8-puzzle is a sliding puzzle consisting of a 3×3 grid containing 8 numbered tiles and one empty space.
The goal is to move the tiles to reach a goal configuration from a given initial configuration by sliding one tile at a time into the empty space.

Example:

Initial State:

1 2 3
4 0 6
7 5 8


Goal State:

1 2 3
4 5 6
7 8 0

⚙️ Techniques Used
1. Breadth First Search (BFS)

Explores all nodes level by level.

Guarantees the shortest solution path.

Uses a queue for traversal.

2. Depth First Search (DFS)

Explores as deep as possible before backtracking.

May not guarantee shortest solution.

Uses recursion or stack.

3. Hill Climbing

Heuristic-based local search.

Always moves towards the neighbor with the lowest heuristic (number of misplaced tiles).

May get stuck in local minima.

4. Heuristic (A) Search*

Combines actual cost (g(n)) and estimated cost to goal (h(n)).

Uses the formula: f(n) = g(n) + h(n)

Finds the optimal path efficiently.

🧩 Heuristic Function Used

h(n) = Number of misplaced tiles (excluding the blank tile 0).

🖥️ Sample Output (BFS Example)
Initial State:
1 2 3
4 0 6
7 5 8

Step 1:
1 2 3
4 5 6
7 0 8

Step 2 (Goal Reached):
1 2 3
4 5 6
7 8 0
