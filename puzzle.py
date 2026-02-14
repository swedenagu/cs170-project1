from queue import PriorityQueue as pq
from array import *
from copy import deepcopy

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

class Puzzle:  # Generic puzzle of size n^2 - 1 elements. We need to keep track of the cost of different moves, the "parent" of each puzzle when we expand from a given game state, the current state of the board, the size of the board, and its neighbors after expansion.
    # don't actually need to track heuristic, that can be calculated in A* star for passed-in state
    def __init__(self, state: list[list[int]], parent=None, move="", cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.size = len(state)
        self.cost = cost

    # don't need to pass in node if calling expand on a Puzzle state already
    # Generates all possible next states of current state that are one move away
    def expand(self):
        neighbors = []
        blank_row, blank_col = self.check_blank()

        # Possible moves are up, down, left, right
        moves = [(-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")]

        for y, x, direction in moves:
            new_row = blank_row + y
            new_col = blank_col + x

            # We should check if the move is valid (doesn't go out of bounds of the board)
            if 0 <= new_row < self.size and 0 <= new_col < self.size:
                # We need to create a new state after moving a tile; we're not changing the original one like a shallow copy would so we should do a deepcopy first
                new_state = deepcopy(self.state)

                # The move happens once we swap the "blank" tile with the adjacent one in the direction we picked
                new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]

                # The new puzzle should then have an increased cost based on the move we just took (all moves have cost of 1)
                neighbor = Puzzle(new_state, parent=self, move=direction, cost = self.cost + 1)
                neighbors.append(neighbor)

        return neighbors
    
    # We need to know the position of the "blank" tile in order to perform an operation (move it in one of four directions)
    def check_blank(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.state[i][j] == 0:
                    return i, j

        return None
    
    # We need to order states in the priority queue by cost -- how do we compare them relatively?
    def __lt__(self, other):
        return self.cost < other.cost
    
    # Does the current state match the goal state?
    def goalCheck(self, goal_state):
        return self.state == goal_state
    
    # Lists aren't hashable (can't be added to set), so we need to convert 2D list (state type) to 2D tuple for visited set to work
    def to_tuple(self):
        return tuple(tuple(row) for row in self.state)
    
    # Prints current puzzle state
    def print_state(self):
        for row in self.state:
            print(row)
        print()
