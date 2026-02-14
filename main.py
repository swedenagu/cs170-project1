from puzzle import Puzzle
from puzzle import trivial, veryEasy, easy, doable, hard
from searches import a_star

def main():
    # Make a puzzle choice
    while True:
        puzzle_mode = input(
            "Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own."
            + "\n"
        )
        if puzzle_mode == "1" or puzzle_mode == "2":
            break
        print("\n")

    # Select a default puzzle or create your own!
    if puzzle_mode == "1":
        print("\nSelect a default puzzle:")
        print("1. Trivial")
        print("2. Very Easy")
        print("3. Easy")
        print("4. Doable")
        print("5. Hard")

        while True:
            selection = input("Enter your choice (1 - 5): ")

            # check puzzle choice input
            puzzles = {"1": trivial, "2": veryEasy, "3": easy, "4": doable, "5": hard}
            if selection in puzzles:
                selected_puzzle = puzzles[selection]
                break

        print("\nSelected puzzle:")

        # display the puzzle selected
        for row in selected_puzzle:
            print(row)
        print()

    # What happens if we select the second puzzle mode?
    else:
        # Enter your own puzzle, using a zero to represent the blank. (this doesn't account for if the size is larger than 3x3, needs to be modified to check length of input row)
        # This should look something like "3 4 5" when entering a series of numbers for a row in the custom starting state.
        puzzle_row_one = input("Enter the first row: ").split()
        puzzle_row_two = input("Enter the second row: ").split()
        puzzle_row_three = input("Enter the third row: ").split()

        # These are entered as strings, we want them as numbers
        puzzle_row_one = [int(x) for x in puzzle_row_one]
        puzzle_row_two = [int(x) for x in puzzle_row_two]
        puzzle_row_three = [int(x) for x in puzzle_row_three]

        selected_puzzle = [puzzle_row_one, puzzle_row_two, puzzle_row_three]

        print("\nYour puzzle:")
        for row in selected_puzzle:
            print(row)
        print()

    # Select algorithm
    while True:
        algorithm = input(
            "Select the algorithm you want to use: (1) Uniform Cost Search, (2) A* with Misplaced Tile heuristic, or (3) A* with Manhattan Distance heuristic\n"
        )
        if algorithm in ["1", "2", "3"]:
            break

    # Next, we need to map the algorithm we picked to its heuristic value. We can pass the result into our general search (A*).
    heuristic_map = {"1": 0, "2": 1, "3": 2}
    heuristic = heuristic_map[algorithm]

    # This isn't strictly necessary but it looks nicer in the initial output; map the name of each algorithm to its respective heuristic
    algorithm_names = {
        0: "Uniform Cost Search",
        1: "A* with Misplaced Tile heuristic",
        2: "A* with Manhattan Distance heuristic",
    }

    print(f"\nRunning {algorithm_names[heuristic]}...\n")

    # Just displayed beforehand, now we actually run the search
    result, nodes_expanded, max_queue_size = a_star(selected_puzzle, heuristic)

    # Display a traceback if solution found
    if result is not None:
        print("Solution traceback")
        print()

        # Build a path from goal state to initial to make it easier to tell what moves were made
        path = []
        current = result
        while current is not None:
            path.append(current)
            current = current.parent

        # Reverse to show start to goal
        path.reverse()

        print(f"\nSolution found in {len(path) - 1} moves:\n")

        for i, puzzle_state in enumerate(path):
            if i == 0:
                print(f"Initial state:")
            else:
                print(f"Move {i}: {puzzle_state.move}")

            puzzle_state.print_state()

        print(f"Total moves: {len(path) - 1}")
        print(f"Nodes expanded: {nodes_expanded}")
        print(f"Max queue size: {max_queue_size}")
    else:
        print("\nNo solution was found.")

if __name__ == "__main__":
    main()
