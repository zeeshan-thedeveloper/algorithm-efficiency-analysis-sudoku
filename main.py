import solver
from time_tracker import TimeTracker
from domains import initialize_domains, print_domains  # Importing the methods

if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents empty cells)
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    # Initialize the time tracker
    timer = TimeTracker()

    # Initialize domains for the Sudoku grid
    domains = initialize_domains(sudoku_grid)
    print("Domains for empty cells before solving:")
    print_domains(domains)  # Print the domains

    # Call the solver and track time
    timer.start()  # Start the timer
    if solver.solve_sudoku(sudoku_grid, domains):  # Pass domains to the solver
        timer.stop()  # Stop the timer if solved
        print("Sudoku solved successfully:")
        solver.print_grid(sudoku_grid)
    else:
        print("No solution exists.")
        timer.stop()  # Stop the timer if no solution exists

    # Output the time taken to solve in milliseconds
    elapsed = timer.elapsed_time()
    print(f"\nTime taken to solve: {elapsed:.2f} milliseconds")
