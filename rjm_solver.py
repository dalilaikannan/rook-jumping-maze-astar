import random
import heapq

def randomize_start_and_goal():
    """
    Returns a random start position and goal position.
    """
    n = len(rjm_grid)
    start = (random.randint(0, n-1), random.randint(0, n-1))
    goal = (random.randint(0, n-1), random.randint(0, n-1))
    return [start, goal]

def calculate_md(pos, goal):
    """
    Calculates and returns the heuristic value from any given (x , y) to the goal.
    This particular example uses the absolute value of Manhattan Distance as the heuristic.
    | (x_goal - x_pos, y_goal, y_pos) | 
    """
    return abs((pos[0] - goal[0]) + (pos[1] - goal[1]))

def get_neighbors(pos):
    """
    Returns all neighbors given a position (x , y). 
    """
    neighbors = []
    jump = rjm_grid[pos[0]][pos[1]]

    # Up
    if pos[0] - jump >= 0:
        neighbors.append((pos[0] - jump, pos[1]))
    # Down
    if pos[0] + jump < len(rjm_grid):
        neighbors.append((pos[0] + jump, pos[1]))
    # Left
    if pos[1] - jump >= 0:
        neighbors.append((pos[0], pos[1] - jump))
    # Right
    if pos[1] + jump < len(rjm_grid):
        neighbors.append((pos[0], pos[1] + jump))

    return neighbors

def a_star_search(start, goal, grid):
    """
    Implements the A* search to find the optimal path from start to goal.
    This particular problem assumes the cost of each jump to be 1.
    Start and goal may be in the same spot, this case is not omitted. 
    """
    # in the queue, heuristic, total cost, current node, path
    tracker = []
    heapq.heappush(tracker, (calculate_md(start, goal), 0, start, [start]))
    visited = set()
    while len(tracker) > 0:
        estimate, total_cost, curr_node, path = heapq.heappop(tracker)

        if curr_node in visited:
            continue
        visited.add(curr_node)

        if curr_node == goal:
            return path
        
        curr_neighbors = get_neighbors(curr_node)
        for i in range(len(curr_neighbors)):
            new_h = calculate_md(curr_neighbors[i], goal)
            new_tc = total_cost + 1
            estimated_cost = new_h + new_tc
            
            heapq.heappush(tracker, (estimated_cost, new_tc, curr_neighbors[i], path + [curr_neighbors[i]]))

    return path

def print_rjm(grid):
    """
    Prints the Rook Jumping Maze in a readable format.
    Each cell shows the number of steps you must jump.
    """
    n = len(grid)
    print("Rook Jumping Maze:")
    print(" ".join([f"{i+1:>3}" for i in range(n)]))  # Column numbers
    print("  +" + "---+"*(n-1))
    for i, row in enumerate(grid):
        row_str = "|".join(f"{cell:>2}" for cell in row)
        print(f"{i+1}|{row_str}|")
        print("  +" + "---+"*(n-1))


# Example RJM 4x4 grid
rjm_grid = [
    [2, 1, 3, 1],
    [1, 2, 1, 2],
    [3, 1, 2, 1],
    [1, 3, 1, 2]
]

# Print the RJM
print_rjm(rjm_grid)
vals = randomize_start_and_goal()
path = a_star_search(vals[0], vals[1], rjm_grid)
print(path)
    