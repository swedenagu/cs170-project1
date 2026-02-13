from queue import PriorityQueue as pq
from treelib import Tree
from array import *

# problem = []
# We can use multiple test cases provided as samples to assess each algorithm
trivial = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
]
veryEasy = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 0, 8],
]
easy = [
    [1, 2, 0],
    [4, 5, 3],
    [7, 8, 6],
]
doable = [
    [0, 1, 2],
    [4, 5, 3],
    [7, 8, 6],
]
hard = [
    [8, 7, 1],
    [6, 0, 2],
    [5, 4, 3],
]
goalState = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
]  # Hardcoded goal state of eight puzzle, used to test if we found solution
puzzles = Tree()


class Puzzle:  # Generic puzzle of size n^2 - 1 elements. We need to keep track of the cost of different moves, the "parent" of each puzzle when we expand from a given game state, the current state of the board, and a way to calculate the heuristic.
    def __init__(self, state: list[list[int]], heuristic: int, parent: list[list[int]], move: str):
        self.state = state
        self.heuristic = heuristic
        self.move = move


# pseudocode
# function general-search(problem, QUEUEING-FUNCTION)
# 	nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE))
# loop do
# if EMPTY(nodes)then return "failure"
# 	node = REMOVE-FRONT(nodes)
# if problem.GOAL-TEST(node.STATE) succeeds then return node
# 	nodes = QUEUEING-FUNCTION(nodes, EXPAND(node, problem.OPERATORS))
# end


def general_search(
    problem: list[list[int]], queuing_function
):  # queuing function implementations are uniform cost search, A* with the
    # Misplaced Tile heuristic, and A* with the Manhattan distance heuristic
    initialState = Puzzle(problem)
    nodes = pq(
        puzzles.create_node("root", data={"state": initialState.state})
    )  # I used a tree implementation to initialize the
    #  first game state of the puzzle, which can be any test case

    while True:
        if (
            not nodes
        ):  # Search function should fail if there are no more game states to explore (no solution!)
            return False  # might need a better return value
        node = nodes.pop()

        if (
            goalState == node.state
        ):  # Are we at the solution yet? Compares goal/solution state to current state of puzzle
            return node.state

        nodes = queuing_function(nodes, expand(node, problem.OPERATORS)
            nodes,
        ) # temporary code until operators and search algorithms are defined


# We need to know the position of the "blank" tile in order to perform an operation (move it in one of four directions)
def check_blank(problem: list[list[int]]):
    for row in problem:
        for col in row:
            if problem[row][col] == 0:
                return row, col

    return None


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

def expand(self, node: Puzzle):
    pass
