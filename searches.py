from queue import PriorityQueue as pq
from puzzle import Puzzle, goalState
import numpy as np

def uniform_cost(search_space: list[list[int]], heuristic: int) -> int: # Uniform cost search
    # The uniform cost search is just A* with the heuristic hardcoded to 0, so it should devolve to breadth-first search by default. We don't need to do anything
    # # Track the initial state with a priority queue, states we're still exploring with a process queue
    # initial_state = Puzzle(search_space)
    # expanding_queue = pq()

    # # We want to track all the nodes we already visited/explored to avoid repeated work
    # visited = set()
    # expanding_queue.put(initial_state)

    # # How many new states are there to explore? Should be capped at a certain amount
    # nodes_expanded = 0
    # max_queue_size = 0
    
    # # repeated_states[starting_node.board_to_tuple()] = "This is the parent board"

    # board_states = [] # We keep track of the stack trace of board states by storing them

    # # stack_to_print = [] # the board states are stored in a stack

    # # while len(working_queue) > 0:
    # #     max_queue_size = max(len(working_queue), max_queue_size)
    # #     # the node from the queue being considered/checked
    # #     node_from_queue = min_heap_esque_queue.heappop(working_queue)
    # #     repeated_states[node_from_queue.board_to_tuple()] = "This can be anything"
    # #     if node_from_queue.solved(): # check if the current state of the board is the solution
    # #         while len(stack_to_print) > 0: # the stack of nodes for the traceback
    # #             print_puzzle(stack_to_print.pop())
    # #         print("Number of nodes expanded:", num_nodes_expanded)
    # #         print("Max queue size:", max_queue_size)
    # #         return node_from_queue
        
    # # stack_to_print.append(node_from_queue.board)
    return 0

def misplaced_tile(search_space: list[list[int]], heuristic: int) -> int: # A* search with Misplaced Tile heuristic
    # Since the heuristic is the number of tiles out of place from the goal state, we can use a counter to track each tile in the puzzle's current state that isn't in the correct position
    count = 0
    
    for row in search_space:
        for col in row:
            if search_space[row][col]!= 0 and search_space[row][col] != goalState[row][col]:
                count += 1

    return count

def manhattan_dist(search_space: list[list[int]], heuristic: int) -> int: # A* search with Manhattan distance heuristic
    # If the cost (1) is the same in all 4 directions we can move, the heuristic is simply the sum of the distances in the x and y direction between the current state and the goal state

    distance = 0
    for row in search_space:
        for col in row:
            if search_space[row][col] != 0:
                # We can make a tuple of arrays, one for each row and column and target the specific value we want using those two dimensions
                goalState_indices = np.where(search_space == search_space[row][col])
                goalState_row = goalState_indices[0][0]
                goalState_col = goalState_indices[1][0]

                # Manhattan distance
                distance += abs(row - goalState_row) + abs(col - goalState_col)

    return distance
