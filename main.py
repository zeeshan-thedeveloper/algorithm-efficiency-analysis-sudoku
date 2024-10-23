# main.py

import solver
import logger 
from time_tracker import TimeTracker
from domains import initialize_domains as domains_init

if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents empty cells)
    logger.start_logging('solver.log')
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

    # Initialize domains
    domains = domains_init(sudoku_grid)
    
    timer = TimeTracker()

    # Call the solver and track time
    use_forward_looking = True  # Set to False if you want to disable forward-looking
    timer.start()  # Start the timer
    if solver.solve_sudoku(sudoku_grid, domains, use_forward_looking):
        timer.stop()  # Stop the timer if solved
        print("Sudoku solved successfully:")
        solver.print_grid(sudoku_grid)
    else:
        print("No solution exists.")
        timer.stop()  # Stop the timer if no solution exists
    is_valid, details = solver.check_sudoku_validity(sudoku_grid)
    if not is_valid:
        print("The Sudoku puzzle is invalid due to the following reasons:")
        for detail in details:
            print(detail)
    else:
        print("The Sudoku puzzle is valid.")
    # Output the time taken to solve in milliseconds
    elapsed = timer.elapsed_time()
    print(f"\nTime taken to solve: {elapsed:.2f} milliseconds")
    logger.stop_logging()
