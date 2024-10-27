
import steps_track
import random
import math
import numpy as np


total_safe_checks = 0

def forward_check(sudoku_grid, domains, row, col, num, verbose=True):
    """Update the domains after assigning a number to a cell."""
    if verbose:
        print(f"Forward checking for value {num} assigned to cell ({row}, {col})")

    for i in range(9):
        # Update domains in the row
        if (row, i) in domains and (row, i) != (row, col) and num in domains[(row, i)]:
            existing_value = sudoku_grid[row][i]  # Get the existing value in the cell
            domains[(row, i)].remove(num)
            if existing_value != 0:
                if verbose:
                    print(f"Domain updated for ROW ({row}, {i}): Removed {num}. Existing value: {existing_value}. New domain: {domains[(row, i)]}")
            else:
                if verbose:
                    print(f"Domain updated for ROW ({row}, {i}): Removed {num}. No existing value (cell was empty). New domain: {domains[(row, i)]}")

        # Update domains in the column
        if (i, col) in domains and (i, col) != (row, col) and num in domains[(i, col)]:
            existing_value = sudoku_grid[i][col]  # Get the existing value in the cell
            domains[(i, col)].remove(num)
            if existing_value != 0:
                if verbose:
                    print(f"Domain updated for COL ({i}, {col}): Removed {num}. Existing value: {existing_value}. New domain: {domains[(i, col)]}")
            else:
                if verbose:
                    print(f"Domain updated for COL ({i}, {col}): Removed {num}. No existing value (cell was empty). New domain: {domains[(i, col)]}")

    # Update domains in the 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            cell = (start_row + i, start_col + j)
            if cell in domains and cell != (row, col) and num in domains[cell]:
                existing_value = sudoku_grid[cell[0]][cell[1]]  # Get the existing value in the cell
                domains[cell].remove(num)
                if existing_value != 0:
                    if verbose:
                        print(f"Domain updated for subgrid cell ({cell[0]}, {cell[1]}): Removed {num}. Existing value: {existing_value}. New domain: {domains[cell]}")
                else:
                    if verbose:
                        print(f"Domain updated for subgrid cell ({cell[0]}, {cell[1]}): Removed {num}. No existing value (cell was empty). New domain: {domains[cell]}")

    # If any cell has no values left in its domain, return False (failure)
    for domain in domains.values():
        if len(domain) == 0:
            return False

    return True

def solve_sudoku(sudoku_grid, domains, use_forward_looking=True, depth=0, verbose=False,search_space_sizes=[]):
    """Solve the Sudoku puzzle using backtracking, with optional forward-looking."""
    empty_cell = find_empty_cell(sudoku_grid)
    if not empty_cell:
        if verbose:
            print(f"{' ' * (depth * 2)}Sudoku solved at depth {depth}!")
        return True  # Sudoku is solved

    row, col = empty_cell
    if verbose:
        print(f"{' ' * (depth * 2)}Exploring Cell ({row}, {col}) at depth {depth}")
    print_domain_for_cell(domains, row, col, verbose)
    
        
    for num in domains.get((row, col), []):
        if is_safe(sudoku_grid, row, col, num, verbose):
            # search_space_sizes.append(total_safe_checks)
            sudoku_grid[row][col] = num
            steps_track.track_step(row, col, num)  # Track the step
            
            if verbose:
                print(f"{' ' * (depth * 2)}Assigned value {num} to Cell ({row}, {col})")

            current_search_space_size = sum(len(v) for v in domains.values())
            search_space_sizes.append(current_search_space_size)

            if use_forward_looking:
                # Perform forward checking to update domains
                new_domains = {k: v[:] for k, v in domains.items()}  # Copy domains
                if forward_check(sudoku_grid, new_domains, row, col, num, verbose):
                    if solve_sudoku(sudoku_grid, new_domains, use_forward_looking, depth + 1, verbose,search_space_sizes):  # Recursive call with forward looking
                        return True
            else:
                # Standard backtracking without forward-looking
                if solve_sudoku(sudoku_grid, domains, use_forward_looking, depth + 1, verbose,search_space_sizes):  # Recursive call without forward-looking
                    return True

            # Reset (backtrack)
            sudoku_grid[row][col] = 0
            if verbose:
                print(f"{' ' * (depth * 2)}Backtracking from Cell ({row}, {col}), resetting value {num}")

    if verbose:
        print(f"{' ' * (depth * 2)}Returning False at depth {depth}, no valid numbers for Cell ({row}, {col})")
    return False


def check_sudoku_validity(sudoku_grid, verbose=True):
    """
    Check the validity of a Sudoku puzzle and report any issues.

    Returns:
        - is_valid: Boolean indicating if the Sudoku is valid.
        - details: List of strings with details of any conflicts found.
    """
    is_valid = True
    details = []

    # Check rows and columns
    for i in range(9):
        row_set = set()
        col_set = set()

        for j in range(9):
            # Check row
            if sudoku_grid[i][j] != 0:
                if sudoku_grid[i][j] in row_set:
                    is_valid = False
                    details.append(f"Duplicate {sudoku_grid[i][j]} found in row {i}.")
                else:
                    row_set.add(sudoku_grid[i][j])

            # Check column
            if sudoku_grid[j][i] != 0:
                if sudoku_grid[j][i] in col_set:
                    is_valid = False
                    details.append(f"Duplicate {sudoku_grid[j][i]} found in column {i}.")
                else:
                    col_set.add(sudoku_grid[j][i])

    # Check subgrids
    for box_row in range(3):
        for box_col in range(3):
            box_set = set()
            for i in range(3):
                for j in range(3):
                    val = sudoku_grid[box_row * 3 + i][box_col * 3 + j]
                    if val != 0:
                        if val in box_set:
                            is_valid = False
                            details.append(f"Duplicate {val} found in subgrid starting at ({box_row * 3}, {box_col * 3}).")
                        else:
                            box_set.add(val)

    # Check for number range validity (1-9)
    for i in range(9):
        for j in range(9):
            val = sudoku_grid[i][j]
            if val < 0 or val > 9:
                is_valid = False
                details.append(f"Invalid value {val} found at cell ({i}, {j}). Values must be between 1 and 9.")

    if verbose and details:
        print("Sudoku validity check details:")
        for detail in details:
            print(detail)

    return is_valid, details

def is_safe(sudoku_grid, row, col, num, verbose=True):
    global total_safe_checks
    checks = 0

    # Check if num is not in the current row
    for x in range(9):
        checks += 1
        if sudoku_grid[row][x] == num:
            if verbose:
                print(f"Value {num} is not safe in row {row}.")
            total_safe_checks += checks  # Track checks
            return False

    # Check if num is not in the current column
    for x in range(9):
        checks += 1
        if sudoku_grid[x][col] == num:
            if verbose:
                print(f"Value {num} is not safe in column {col}.")
            total_safe_checks += checks  # Track checks
            return False

    # Check if num is not in the current 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            checks += 1
            if sudoku_grid[i + start_row][j + start_col] == num:
                if verbose:
                    print(f"Value {num} is not safe in subgrid starting at ({start_row}, {start_col}).")
                total_safe_checks += checks  # Track checks
                return False

    total_safe_checks += checks  # Track total checks
    return True

def print_domain_for_cell(domains, row, col, verbose=True):
    """Print the domain for the given empty cell (row, col)."""
    if verbose:
        if (row, col) in domains:
            print(f"Cell ({row}, {col}): Possible values {domains[(row, col)]}")
        else:
            print(f"Cell ({row}, {col}): No domain found (already filled or invalid).")

def find_empty_cell(sudoku_grid):
    for i in range(9):
        for j in range(9):
            if sudoku_grid[i][j] == 0:
                return (i, j)  # Return the row and column of the empty cell
    return None

def print_grid(sudoku_grid, verbose=True):
    if verbose:
        for row in sudoku_grid:
            print(" ".join(str(num) for num in row))
