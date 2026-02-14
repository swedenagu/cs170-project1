from queue import PriorityQueue as pq
from puzzle import Puzzle, goalState
import numpy as np

def uniform_cost(search_space: list[list[int]]) -> int: # Uniform cost search
    # The uniform cost search is just A* with the heuristic hardcoded to 0, so it should devolve to breadth-first search by default. We don't need to do anything
    return 0

def misplaced_tile(search_space: list[list[int]]) -> int: # A* search with Misplaced Tile heuristic
    # Since the heuristic is the number of tiles out of place from the goal state, we can use a counter to track each tile in the puzzle's current state that isn't in the correct position
    count = 0
    
    for i in range(len(search_space)):
        for j in range(len(search_space)):
            if search_space[i][j]!= 0 and search_space[i][j] != goalState[i][j]:
                count += 1

    return count

def manhattan_dist(search_space: list[list[int]]) -> int: # A* search with Manhattan distance heuristic
    # If the cost (1) is the same in all 4 directions we can move, the heuristic is simply the sum of the distances in the x and y direction between the current state and the goal state

    distance = 0
    for i in range(len(search_space)):
        for j in range(len(search_space)):
            if search_space[i][j] != 0:
                # We can make a tuple of arrays, one for each row and column and target the specific value we want using those two dimensions
                goalState_indices = np.where(goalState == search_space[i][j])
                goalState_row = goalState_indices[0][0]
                goalState_col = goalState_indices[1][0]

                # Manhattan distance
                distance += abs(i - goalState_row) + abs(j - goalState_col)

    return distance

# the goal state wasn't really needed as a parameter so I took it out
def a_star(search_space, heuristic: int):
    # pseudocode
    # function general-search(problem, QUEUEING-FUNCTION)
    # 	nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE))
    # loop do
    # if EMPTY(nodes)then return "failure"
    # 	node = REMOVE-FRONT(nodes)
    # if problem.GOAL-TEST(node.STATE) succeeds then return node
    # 	nodes = QUEUEING-FUNCTION(nodes, EXPAND(node, problem.OPERATORS))
    # end

    # Track the initial state with a priority queue, states we're still exploring with a process queue
    initial_state = Puzzle(search_space)
    expanding_queue = pq()

    # We want to track all the nodes we already visited/explored to avoid repeated work
    visited = set()
    nodes_expanded = 0
    max_queue_size = 0
    counter = 0

    # Find the initial heuristic
    if heuristic == 1:
        h = uniform_cost(initial_state.state)
    elif heuristic == 2:
        h = misplaced_tile(initial_state.state)
    elif heuristic == 3:
        h = manhattan_dist(initial_state.state)

    # Adds a tuple with given total estimated cost to move, counter of nodes, and initial state
    # not supposed to hardcode to zero heuristic like in uniform cost search, wouldn't be complete
    expanding_queue.put((h + initial_state.cost, counter, initial_state))
    counter += 1

    while expanding_queue:
        max_queue_size = max(len(expanding_queue), max_queue_size)

        # We want to look at the puzzle with the lowest combined heuristic and cost next
        # have placeholder values for tuple instead of popping from priority queue without type checking
        _, _, current = expanding_queue.get()

        # This makes sure we don't go to a state we already visited
        if current.to_tuple() in visited:
            continue

        visited.add(current.to_tuple())
        nodes_expanded += 1

        if heuristic == 1:
            h = uniform_cost(current.state)
        elif heuristic == 2:
            h = misplaced_tile(current.state)
        elif heuristic == 3:
            h = manhattan_dist(current.state)

        # Did we reach the goal state yet?
        if current.goalCheck(goalState):
            print("\nGoal reached!")
            print(f"Solution depth was {current.cost}")
            print(f"Number of nodes expanded: {nodes_expanded}")
            print(f"Max queue size: {max_queue_size}")
            print("\nGoal state:")
            current.print_state()

            return current, nodes_expanded, max_queue_size

        # Find neighbors to explore next
        for neighbor in current.nearest:
            if neighbor.to_tuple() not in visited:
                # Find the heuristic for neighboring node
                if heuristic == 1:
                    h = uniform_cost(neighbor.state)
                elif heuristic == 2:
                    h = misplaced_tile(neighbor.state)
                elif heuristic == 3:
                    h = manhattan_dist(neighbor.state)

                priority = neighbor.cost + h
                expanding_queue.put((priority, counter, neighbor))
                counter += 1

    return None, nodes_expanded, max_queue_size
