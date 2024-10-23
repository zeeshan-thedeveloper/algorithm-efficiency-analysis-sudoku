def initialize_domains(sudoku_grid):
    """
    Initialize domains for all empty cells in the Sudoku grid.
    Each empty cell will have a domain of possible values (1-9).
    """
    domains = {}

    # Iterate through the Sudoku grid
    for i in range(9):  # Rows
        for j in range(9):  # Columns
            if sudoku_grid[i][j] == 0:  # Check for empty cell
                # Initialize the domain with all possible values (1-9)
                domains[(i, j)] = list(range(1, 10))

    return domains

def print_domains(domains):
    """
    Print the domains of each empty cell.
    """
    for position, domain in domains.items():
        print(f"Cell {position} has possible values: {domain}")

