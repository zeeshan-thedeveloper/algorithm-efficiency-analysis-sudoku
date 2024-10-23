# steps-track.py

steps = []  # Global list to store steps

# Function to track a step
def track_step(row, col, num):
    steps.append(f"Placed {num} at ({row}, {col})")

# Function to retrieve all tracked steps
def get_steps():
    return steps
