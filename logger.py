import sys

class Logger:
    def __init__(self, log_file='solver.log'):
        self.terminal = sys.stdout
        self.log = open(log_file, 'a')  # Open the log file in append mode

    def write(self, message):
        self.terminal.write(message)  # Print to the console
        self.log.write(message)  # Write to the log file

    def flush(self):
        pass  # This method is needed for compatibility with sys.stdout

# Initialize the logger
def start_logging(log_file='solver.log'):
    sys.stdout = Logger(log_file)

# Stop logging (optional, if you want to switch back to the normal console output)
def stop_logging():
    sys.stdout = sys.__stdout__  # Reset back to default stdout
