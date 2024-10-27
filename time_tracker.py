# time_tracker.py

import time

class TimeTracker:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()  # Get current time in seconds

    def stop(self):
        self.end_time = time.time()  # Get current time in seconds

    def elapsed_time(self):
        """Return the elapsed time in milliseconds."""
        if self.start_time is None or self.end_time is None:
            return 0
        return (self.end_time - self.start_time)   # Convert to milliseconds
