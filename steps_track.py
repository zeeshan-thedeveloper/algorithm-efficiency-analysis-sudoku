steps = []  # Global list to store steps
backtrack_steps = []  # Global list to store backtracking steps

# Function to track a step when a number is placed
def track_step(row, col, num):
    steps.append(f"Placed {num} at ({row}, {col})")

# Function to track backtracking
def track_backtrack(row, col, num):
    backtrack_steps.append(f"Backtracked from value {num} at ({row}, {col})")

# Function to retrieve all tracked steps
def get_steps():
    return steps

# Function to retrieve all backtracking steps
def get_backtrack_steps():
    return backtrack_steps

# Function to reset the tracking lists (for fresh starts)
def reset_tracking():
    global steps, backtrack_steps
    steps = []
    backtrack_steps = []
