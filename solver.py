# solver.py

import steps_track

def is_safe(sudoku_grid, row, col, num):
    # Check if num is not in the current row
    for x in range(9):
        if sudoku_grid[row][x] == num:
            return False

    # Check if num is not in the current column
    for x in range(9):
        if sudoku_grid[x][col] == num:
            return False

    # Check if num is not in the current 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku_grid[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(sudoku_grid, domains):
    empty_cell = find_empty_cell(sudoku_grid)
    if not empty_cell:
        return True  # Sudoku is solved
    row, col = empty_cell

    # Use the domain for the current empty cell
    for num in domains.get((row, col), []):
        if is_safe(sudoku_grid, row, col, num):
            sudoku_grid[row][col] = num
            steps_track.track_step(row, col, num)  # Track the step

            if solve_sudoku(sudoku_grid, domains):  # Recursive call
                return True

            sudoku_grid[row][col] = 0  # Reset (backtrack)

    return False

def find_empty_cell(sudoku_grid):
    for i in range(9):
        for j in range(9):
            if sudoku_grid[i][j] == 0:
                return (i, j)  # Return the row and column of the empty cell
    return None

def print_grid(sudoku_grid):
    for row in sudoku_grid:
        print(" ".join(str(num) for num in row))
