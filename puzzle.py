from queue import PriorityQueue as pq
from treelib import Tree
from array import *

problem = []
goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] # Hardcoded goal state of eight puzzle, used to test if we found solution
puzzles = Tree()

class Puzzle: # Generic puzzle of size n^2 - 1
    def __init__(self, state: list[list[int]]):
        self.state = state

    def __str__(self):
        return self.join(map(str, self))

# pseudocode
# function general-search(problem, QUEUEING-FUNCTION)
# 	nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE))
# loop do
# if EMPTY(nodes)then return "failure"
# 	node = REMOVE-FRONT(nodes)
# if problem.GOAL-TEST(node.STATE) succeeds then return node
# 	nodes = QUEUEING-FUNCTION(nodes, EXPAND(node, problem.OPERATORS))
# end

def general_search(problem: list[list[int]], queuing_function): # queuing function implementations are uniform cost search, A* with the
                                               # Misplaced Tile heuristic, and A* with the Manhattan distance heuristic
    initialState = Puzzle(problem)
    nodes = pq(puzzles.create_node("root", data={"state": initialState.state})) # I used a tree implementation to initialize the
                                             #  first game state of the puzzle, which can be any test case

    while (True):
        if not nodes: # Search function should fail if there are no more game states to explore (no solution!)
            return False # might need a better return value
        node = nodes.pop()

        if (goalState == node.state): # Are we at the solution yet? Compares goal/solution state to current state of puzzle
            return node.state
        
        nodes = uniform_cost(nodes, )


# def move_up(problem: list[list[int]]) -> list[list[int]]:
#     for row in problem:
#         for col in row:
#             if problem[row][col] == 0:
#                 if row > 0:
#                     problem[row-1][col], problem[row][col] = problem[row][col], problem[row-1][col]

#     return problem

# def move_down(problem: list[list[int]]) -> list[list[int]]:
#     for row in problem:
#         for col in row:
#             if problem[row][col] == 0:
#                 if row < len(problem) - 1:
#                     problem[row+1][col], problem[row][col] = problem[row][col], problem[row+1][col]

#     return problem

# def move_left(problem: list[list[int]]) -> list[list[int]]:
#     for row in problem:
#         for col in row:
#             if problem[row][col] == 0:
#                 if col > 0:
#                     problem[row][col-1], problem[row][col] = problem[row][col], problem[row][col-1]

#     return problem

# def move_right(problem: list[list[int]]) -> list[list[int]]:
#     for row in problem:
#         for col in row:
#             if problem[row][col] == 0:
#                 if col < len(problem[0]) - 1:
#                     problem[row][col+1], problem[row][col] = problem[row][col], problem[row][col+1]

#     return problem

def expand(head: Puzzle): # Creates all children of current node "head" where each child is a different single operator applied
                    # to input state
    puzzles.create_node(data={"state": move_left(head.state)})
    puzzles.create_node(data={"state": move_right(head.state)})
    puzzles.create_node(data={"state": move_up(head.state)})
    puzzles.create_node(data={"state": move_down(head.state)})
