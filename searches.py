from queue import PriorityQueue as pq

def uniform_cost(search_space: list[list[int]], heuristic: int): # Uniform cost search
    # Track the initial state with a priority queue, states we're still exploring with a process queue
    priority_queue = pq()
    expanding_queue = []

    # Which nodes have we explored already? We want to minimize repeated work
    visited = set()
    # min_heap_esque_queue.heappush(working_queue, starting_node)
    # num_nodes_expanded = 0
    # max_queue_size = 0
    # repeated_states[starting_node.board_to_tuple()] = "This is the parent board"

    # stack_to_print = [] # the board states are stored in a stack

    # while len(working_queue) > 0:
    #     max_queue_size = max(len(working_queue), max_queue_size)
    #     # the node from the queue being considered/checked
    #     node_from_queue = min_heap_esque_queue.heappop(working_queue)
    #     repeated_states[node_from_queue.board_to_tuple()] = "This can be anything"
    #     if node_from_queue.solved(): # check if the current state of the board is the solution
    #         while len(stack_to_print) > 0: # the stack of nodes for the traceback
    #             print_puzzle(stack_to_print.pop())
    #         print("Number of nodes expanded:", num_nodes_expanded)
    #         print("Max queue size:", max_queue_size)
    #         return node_from_queue
        
    # stack_to_print.append(node_from_queue.board)
    pass

def misplaced_tile(search_space: list[list[int]], ): # A* search with Misplaced Tile heuristic
    pass

def manhattan_dist(search_space: list[list[int]], ): # A* search with Manhattan distance heuristic
    pass
