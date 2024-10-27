# import solver
# import logger 
# from time_tracker import TimeTracker
# from domains import initialize_domains as domains_init
# from simulated_anealing_solver import simulated_annealing  # Adjust the import according to your file structure
# import matplotlib.pyplot as plt  # Import matplotlib for plotting
# import copy  # Import copy for deep copying
# import numpy as np
# from memory_profiler import memory_usage


# def solve_with_memory_tracking(solver_function, *args, **kwargs):
#     # Track memory usage and execution time
#     timer = TimeTracker()
#     timer.start()
    
#     mem_usage = memory_usage((solver_function, args, kwargs), interval=0.1)
    
#     timer.stop()
#     elapsed_time = timer.elapsed_time()
    
#     return elapsed_time, max(mem_usage)  # Return time taken and max memory usage

# if __name__ == "__main__":
#     logger.start_logging('solver.log')

#     sudoku_grid = [
#         [0, 0, 5, 3, 0, 0, 0, 0, 0],
#         [8, 0, 0, 0, 0, 0, 0, 2, 0],
#         [0, 7, 0, 0, 1, 0, 5, 0, 0],
#         [4, 0, 0, 0, 0, 5, 3, 0, 0],
#         [0, 1, 0, 7, 0, 0, 0, 0, 6],
#         [0, 0, 3, 0, 0, 0, 0, 0, 2],
#         [0, 6, 0, 0, 0, 0, 0, 8, 0],
#         [0, 0, 0, 0, 2, 0, 0, 0, 3],
#         [0, 0, 0, 5, 0, 0, 7, 4, 0]
#     ]

#     # Initialize domains
#     domains = domains_init(sudoku_grid)

#     times_backtracking = []  # List to store times for backtracking solver without forward checking
#     times_backtracking_fc = []  # List to store times for backtracking solver with forward checking
#     times_sa = []            # List to store times for simulated annealing
#     temperatures = []        # List to store temperatures for simulated annealing
#     sa_times = []            # List to store times for simulated annealing with varying temperatures

#     attempts = 0  # Number of attempts for backtracking and simulated annealing
#     sa_attempts = 20  # Number of attempts for simulated annealing temperature variation

#     # # Run for the main backtracking and simulated annealing
#     for attempt in range(attempts):
#         # Create deep copies of the grid and domains for each attempt
#         current_sudoku_grid = copy.deepcopy(sudoku_grid)
#         domains = domains_init(current_sudoku_grid)

#         # Run Backtracking Solver without Forward Checking
#         timer = TimeTracker()  # Create a new timer for backtracking
#         timer.start()  # Start the timer

#         if solver.solve_sudoku(current_sudoku_grid, domains, False, 0, False):
#             timer.stop()  # Stop the timer if solved
#             elapsed_backtracking = timer.elapsed_time()  # Get the elapsed time for backtracking
#             print(f"Attempt {attempt + 1} (Backtracking): Sudoku solved successfully.")
#         else:
#             timer.stop()  # Stop the timer if no solution exists
#             elapsed_backtracking = timer.elapsed_time()
#             print(f"Attempt {attempt + 1} (Backtracking): No solution exists.")
        
#         times_backtracking.append(elapsed_backtracking)  # Append the time taken for backtracking

#         # Create deep copies of the grid and domains for the backtracking with forward checking
#         current_sudoku_grid_fc = copy.deepcopy(sudoku_grid)
#         domains_fc = domains_init(current_sudoku_grid_fc)

#         # Run Backtracking Solver with Forward Checking
#         timer = TimeTracker()  # Create a new timer for backtracking with forward checking
#         timer.start()  # Start the timer

#         if solver.solve_sudoku(current_sudoku_grid_fc, domains_fc, True, 0, False):
#             timer.stop()  # Stop the timer if solved
#             elapsed_backtracking_fc = timer.elapsed_time()  # Get the elapsed time for backtracking with forward checking
#             print(f"Attempt {attempt + 1} (Backtracking with FC): Sudoku solved successfully.")
#         else:
#             timer.stop()  # Stop the timer if no solution exists
#             elapsed_backtracking_fc = timer.elapsed_time()
#             print(f"Attempt {attempt + 1} (Backtracking with FC): No solution exists.")

#         times_backtracking_fc.append(elapsed_backtracking_fc)  # Append the time taken for backtracking with forward checking

#         # Create deep copies of the grid for Simulated Annealing
#         current_sudoku_grid_sa = copy.deepcopy(sudoku_grid)

#         # Run Simulated Annealing Solver
#         timer = TimeTracker()  # Create a new timer for simulated annealing
#         timer.start()  # Start the timer

#         solved_grid = simulated_annealing(current_sudoku_grid_sa, initial_temp=400000, cooling_rate=0.999)  # Run simulated annealing
#         timer.stop()  # Stop the timer
#         elapsed_sa = timer.elapsed_time()  # Get the elapsed time for simulated annealing

#         if solved_grid is not None and solved_grid.size > 0:
#             print(f"Attempt {attempt + 1} (Simulated Annealing): Sudoku solved successfully.")
#         else:
#             print(f"Attempt {attempt + 1} (Simulated Annealing): No solution found.")

#         times_sa.append(elapsed_sa)  # Append the time taken for simulated annealing

#     # # Output all times taken
#     # print("\nTimes taken for each attempt:")
#     # print("\nBacktracking Solver Times (milliseconds):")
#     # for i, time_taken in enumerate(times_backtracking):
#     #     print(f"Attempt {i + 1}: {time_taken:.2f} ms")

#     # print("\nBacktracking Solver with Forward Checking Times (milliseconds):")
#     # for i, time_taken in enumerate(times_backtracking_fc):
#     #     print(f"Attempt {i + 1}: {time_taken:.2f} ms")

#     # print("\nSimulated Annealing Times (milliseconds):")
#     # for i, time_taken in enumerate(times_sa):
#     #     print(f"Attempt {i + 1}: {time_taken:.2f} ms")

#     # # --- Simulated Annealing Temperature Variation ---
#     # initial_temps = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000, 1500000, 1600000]   # 10 samples of temperatures

#     # for temp in initial_temps:
#     #     temperatures.append(temp)  # Store the temperature
#     #     # Create deep copies of the grid for each temperature
#     #     current_sudoku_grid_temp = copy.deepcopy(sudoku_grid)

#     #     # Run Simulated Annealing Solver with the current temperature
#     #     timer = TimeTracker()  # Create a new timer for simulated annealing
#     #     timer.start()  # Start the timer

#     #     solved_grid = simulated_annealing(current_sudoku_grid_temp, initial_temp=temp, cooling_rate=0.999)  # Run simulated annealing
#     #     timer.stop()  # Stop the timer
#     #     elapsed_temp_sa = timer.elapsed_time()  # Get the elapsed time for simulated annealing

#     #     sa_times.append(elapsed_temp_sa)  # Append the time taken for simulated annealing with varying temperatures

#     # Create a more comprehensive list of cooling rates from 0.1 to 1.0
#     cooling_rates = np.arange(0.1, 0.99, 0.1)  # Generates values from 0.1 to 1.0 in steps of 0.01
#     times_sa = []  # List to store times for simulated annealing

#     # Run simulated annealing for different cooling rates
#     for cooling_rate in cooling_rates:
#         timer = TimeTracker()  # Create a new timer for simulated annealing
#         timer.start()  # Start the timer

#         # Run simulated annealing with the current cooling rate
#         elapsed_sa, max_memory_sa = solve_with_memory_tracking(simulated_annealing, sudoku_grid, initial_temp=400000, cooling_rate=cooling_rate)

#         if elapsed_sa > 0:  # Check if the solver function ran without errors
#             print(f"Simulated Annealing with Cooling Rate {cooling_rate:.2f}: Sudoku solved successfully in {elapsed_sa:.2f} ms with max memory usage of {max_memory_sa:.2f} MiB.")
#         else:
#             print(f"Simulated Annealing with Cooling Rate {cooling_rate:.2f}: No solution found.")

#         solved_grid = simulated_annealing(sudoku_grid, initial_temp=400000, cooling_rate=cooling_rate)
#         timer.stop()  # Stop the timer
#         elapsed_sa = timer.elapsed_time()  # Get the elapsed time for simulated annealing

#         if solved_grid is not None and solved_grid.size > 0:
#             print(f"Simulated Annealing with Cooling Rate {cooling_rate:.2f}: Sudoku solved successfully.")
#         else:
#             print(f"Simulated Annealing with Cooling Rate {cooling_rate:.2f}: No solution found.")

#         times_sa.append(elapsed_sa)  # Append the time taken for simulated annealing

#     # Output all times taken for simulated annealing
#     print("\nSimulated Annealing Times (milliseconds):")
#     for i, time_taken in enumerate(times_sa):
#         print(f"Cooling Rate {cooling_rates[i]:.2f}: {time_taken:.2f} ms")

#     # Plotting results
#     plt.figure(figsize=(10, 6))
#     plt.plot(cooling_rates, times_sa, marker='o')
#     plt.title('Time Taken by Simulated Annealing vs Cooling Rate')
#     plt.xlabel('Cooling Rate')
#     plt.ylabel('Time Taken (ms)')
#     plt.grid()
#     plt.show()
    
    
#     # # Plotting the results for Backtracking Solver without Forward Checking
#     # plt.figure(figsize=(8, 4))
#     # plt.plot(range(1, attempts + 1), times_backtracking, marker='o', color='blue', label='Backtracking')
#     # plt.title('Backtracking Solver Execution Times')
#     # plt.xlabel('Attempt Number')
#     # plt.ylabel('Time (milliseconds)')
#     # plt.xticks(range(1, attempts + 1))
#     # plt.grid()
#     # plt.legend()
#     # plt.tight_layout()
#     # plt.savefig('backtracking_solver_times.png')  # Save the figure as a .png file
#     # plt.show()

#     # # Plotting the results for Backtracking Solver with Forward Checking
#     # plt.figure(figsize=(8, 4))
#     # plt.plot(range(1, attempts + 1), times_backtracking_fc, marker='o', color='green', label='Backtracking with FC')
#     # plt.title('Backtracking Solver with Forward Checking Execution Times')
#     # plt.xlabel('Attempt Number')
#     # plt.ylabel('Time (milliseconds)')
#     # plt.xticks(range(1, attempts + 1))
#     # plt.grid()
#     # plt.legend()
#     # plt.tight_layout()
#     # plt.savefig('backtracking_solver_fc_times.png')  # Save the figure as a .png file
#     # plt.show()

#     # # Plotting the results for Simulated Annealing Solver
#     # plt.figure(figsize=(8, 4))
#     # plt.plot(range(1, attempts + 1), times_sa, marker='o', color='red', label='Simulated Annealing')
#     # plt.title('Simulated Annealing Solver Execution Times')
#     # plt.xlabel('Attempt Number')
#     # plt.ylabel('Time (milliseconds)')
#     # plt.xticks(range(1, attempts + 1))
#     # plt.grid()
#     # plt.legend()
#     # plt.tight_layout()
#     # plt.savefig('simulated_annealing_solver_times.png')  # Save the figure as a .png file
#     # plt.show()

#     # # --- Plotting Temperature vs Time for Simulated Annealing ---
#     # plt.figure(figsize=(8, 4))
#     # plt.plot(temperatures, sa_times, marker='o', color='purple', label='Simulated Annealing Times')
#     # plt.title('Simulated Annealing: Temperature vs Time to Solve')
#     # plt.xlabel('Initial Temperature')
#     # plt.ylabel('Time (milliseconds)')
#     # plt.xticks(temperatures, rotation=45)
#     # plt.grid()
#     # plt.legend()
#     # plt.tight_layout()
#     # plt.savefig('simulated_annealing_temp_vs_time.png')  # Save the figure as a .png file
#     # plt.show()

#     # Stop logging
#     logger.stop_logging()


# =========================Time Taken by Simulated Annealing vs Cooling Rate==============

# import solver
# import logger 
# from time_tracker import TimeTracker
# from domains import initialize_domains as domains_init
# from simulated_anealing_solver import simulated_annealing  
# import matplotlib.pyplot as plt  
# import copy  
# import numpy as np
# from memory_profiler import memory_usage


# def solve_with_memory_tracking(solver_function, *args, **kwargs):
#     # Track memory usage and execution time
#     timer = TimeTracker()
#     timer.start()
    
#     mem_usage = memory_usage((solver_function, args, kwargs), interval=0.1)
    
#     timer.stop()
#     elapsed_time = timer.elapsed_time()
    
#     return elapsed_time, max(mem_usage)  # Return time taken and max memory usage

# if __name__ == "__main__":
#     logger.start_logging('solver.log')

#     sudoku_grid = [
#            [8, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 3, 6, 0, 0, 0, 0, 0],
#     [0, 7, 0, 0, 9, 0, 2, 0, 0],
#     [0, 5, 0, 0, 0, 7, 0, 0, 0],
#     [0, 0, 0, 0, 4, 5, 7, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 3, 0],
#     [0, 0, 1, 0, 0, 0, 0, 6, 8],
#     [0, 0, 8, 5, 0, 0, 0, 1, 0],
#     [0, 9, 0, 0, 0, 0, 4, 0, 0]
#     ]

#     # Initialize domains
#     domains = domains_init(sudoku_grid)

#     times_backtracking = []  
#     max_memory_backtracking = []  
#     times_backtracking_fc = []  
#     max_memory_backtracking_fc = []  
#     times_sa = []            
#     max_memory_sa = []       
#     cooling_rates = np.arange(0.1, 0.99, 0.1)  

#     attempts = 20  # Number of attempts for backtracking and simulated annealing

#     # Run for the main backtracking and simulated annealing
#     for attempt in range(attempts):
#         # Create deep copies of the grid and domains for each attempt
#         current_sudoku_grid = copy.deepcopy(sudoku_grid)
#         domains = domains_init(current_sudoku_grid)

#         # Run Backtracking Solver without Forward Checking
#         elapsed_backtracking, max_memory_bt = solve_with_memory_tracking(solver.solve_sudoku, current_sudoku_grid, domains, False, 0, False)

#         if elapsed_backtracking > 0:  # Check if solved
#             print(f"Attempt {attempt + 1} (Backtracking): Sudoku solved successfully.")
#         else:
#             print(f"Attempt {attempt + 1} (Backtracking): No solution exists.")
        
#         times_backtracking.append(elapsed_backtracking)  
#         max_memory_backtracking.append(max_memory_bt)  # Store max memory usage

#         # Create deep copies of the grid and domains for the backtracking with forward checking
#         current_sudoku_grid_fc = copy.deepcopy(sudoku_grid)
#         domains_fc = domains_init(current_sudoku_grid_fc)

#         # Run Backtracking Solver with Forward Checking
#         elapsed_backtracking_fc, max_memory_bt_fc = solve_with_memory_tracking(solver.solve_sudoku, current_sudoku_grid_fc, domains_fc, True, 0, False)

#         if elapsed_backtracking_fc > 0:  # Check if solved
#             print(f"Attempt {attempt + 1} (Backtracking with FC): Sudoku solved successfully.")
#         else:
#             print(f"Attempt {attempt + 1} (Backtracking with FC): No solution exists.")

#         times_backtracking_fc.append(elapsed_backtracking_fc)  
#         max_memory_backtracking_fc.append(max_memory_bt_fc)  # Store max memory usage

#         # Create deep copies of the grid for Simulated Annealing
#         current_sudoku_grid_sa = copy.deepcopy(sudoku_grid)

#         # Run Simulated Annealing Solver
#         elapsed_sa, max_memory_sa_current = solve_with_memory_tracking(simulated_annealing, current_sudoku_grid_sa, initial_temp=400000, cooling_rate=0.999)

#         if elapsed_sa > 0:  # Check if solved
#             print(f"Attempt {attempt + 1} (Simulated Annealing): Sudoku solved successfully.")
#         else:
#             print(f"Attempt {attempt + 1} (Simulated Annealing): No solution found.")

#         times_sa.append(elapsed_sa)  # Append the time taken for simulated annealing
#         max_memory_sa.append(max_memory_sa_current)  # Store max memory usage for simulated annealing

#     # Output all times and memory usage taken
#     print("\nBacktracking Solver Times (milliseconds):")
#     for i, time_taken in enumerate(times_backtracking):
#         print(f"Attempt {i + 1}: {time_taken:.2f} ms, Max Memory: {max_memory_backtracking[i]:.2f} MiB")

#     print("\nBacktracking Solver with Forward Checking Times (milliseconds):")
#     for i, time_taken in enumerate(times_backtracking_fc):
#         print(f"Attempt {i + 1}: {time_taken:.2f} ms, Max Memory: {max_memory_backtracking_fc[i]:.2f} MiB")

#     print("\nSimulated Annealing Times (milliseconds):")
#     for i, time_taken in enumerate(times_sa):
#         print(f"Cooling Rate {cooling_rates[i]:.2f}: {time_taken:.2f} ms, Max Memory: {max_memory_sa[i]:.2f} MiB")

#     # Plotting results
#     plt.figure(figsize=(10, 6))
#     plt.plot(cooling_rates, times_sa, marker='o')
#     plt.title('Time Taken by Simulated Annealing vs Cooling Rate')
#     plt.xlabel('Cooling Rate')
#     plt.ylabel('Time Taken (ms)')
#     plt.grid()
#     plt.show()

#     # Stop logging
#     logger.stop_logging()

# ==============simulated anealing,bt,bt-fc memory===============


# import solver
# import logger
# from time_tracker import TimeTracker
# from domains import initialize_domains as domains_init
# from simulated_anealing_solver import simulated_annealing  # Adjust the import according to your file structure
# import matplotlib.pyplot as plt  # Import matplotlib for plotting
# import copy  # Import copy for deep copying
# import numpy as np
# from memory_profiler import memory_usage


# def solve_with_memory_tracking(solver_function, *args, **kwargs):
#     # Track memory usage and execution time
#     timer = TimeTracker()
#     timer.start()
    
#     mem_usage = memory_usage((solver_function, args, kwargs), interval=0.1)
    
#     timer.stop()
#     elapsed_time = timer.elapsed_time()
    
#     return elapsed_time, max(mem_usage)  # Return time taken and max memory usage


# if __name__ == "__main__":
#     logger.start_logging('solver.log')

#     sudoku_grid = [
    #    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 3, 6, 0, 0, 0, 0, 0],
    # [0, 7, 0, 0, 9, 0, 2, 0, 0],
    # [0, 5, 0, 0, 0, 7, 0, 0, 0],
    # [0, 0, 0, 0, 4, 5, 7, 0, 0],
    # [0, 0, 0, 1, 0, 0, 0, 3, 0],
    # [0, 0, 1, 0, 0, 0, 0, 6, 8],
    # [0, 0, 8, 5, 0, 0, 0, 1, 0],
    # [0, 9, 0, 0, 0, 0, 4, 0, 0]
#     ]

#     # Initialize domains
#     domains = domains_init(sudoku_grid)

#     times_backtracking = []  # List to store times for backtracking solver without forward checking
#     times_backtracking_fc = []  # List to store times for backtracking solver with forward checking
#     times_sa = []            # List to store times for simulated annealing
#     mem_backtracking = []     # List to store memory usage for backtracking solver
#     mem_backtracking_fc = []  # List to store memory usage for backtracking with forward checking
#     mem_sa = []              # List to store memory usage for simulated annealing

#     attempts = 10  # Number of attempts for backtracking and simulated annealing

#     for attempt in range(attempts):
#         print(attempt)
#         # Create deep copies of the grid and domains for each attempt
#         current_sudoku_grid = copy.deepcopy(sudoku_grid)
#         domains = domains_init(current_sudoku_grid)

#         # Run Backtracking Solver without Forward Checking
#         elapsed_backtracking, max_mem_backtracking = solve_with_memory_tracking(
#             solver.solve_sudoku, current_sudoku_grid, domains, False, 0, False
#         )
#         times_backtracking.append(elapsed_backtracking)
#         mem_backtracking.append(max_mem_backtracking)

#         # Create deep copies of the grid and domains for the backtracking with forward checking
#         current_sudoku_grid_fc = copy.deepcopy(sudoku_grid)
#         domains_fc = domains_init(current_sudoku_grid_fc)

#         # Run Backtracking Solver with Forward Checking
#         elapsed_backtracking_fc, max_mem_backtracking_fc = solve_with_memory_tracking(
#             solver.solve_sudoku, current_sudoku_grid_fc, domains_fc, True, 0, False
#         )
#         times_backtracking_fc.append(elapsed_backtracking_fc)
#         mem_backtracking_fc.append(max_mem_backtracking_fc)

#         # Create deep copies of the grid for Simulated Annealing
#         current_sudoku_grid_sa = copy.deepcopy(sudoku_grid)

#         # Run Simulated Annealing Solver
#         elapsed_sa, max_mem_sa = solve_with_memory_tracking(
#             simulated_annealing, current_sudoku_grid_sa, initial_temp=400000, cooling_rate=0.999
#         )
#         times_sa.append(elapsed_sa)
#         mem_sa.append(max_mem_sa)

#     # Output all memory usage for each attempt
#     print("\nMemory Usage (MiB):")
#     for i in range(attempts):
#         print(f"Attempt {i + 1}: Backtracking: {mem_backtracking[i]:.2f}, Backtracking FC: {mem_backtracking_fc[i]:.2f}, Simulated Annealing: {mem_sa[i]:.2f}")

#     # Plotting memory usage results
#     plt.figure(figsize=(10, 6))
#     plt.plot(range(1, attempts + 1), mem_backtracking, marker='o', color='blue', label='Backtracking')
#     plt.plot(range(1, attempts + 1), mem_backtracking_fc, marker='o', color='green', label='Backtracking with FC')
#     plt.plot(range(1, attempts + 1), mem_sa, marker='o', color='red', label='Simulated Annealing')
#     plt.title('Memory Usage of Sudoku Solvers')
#     plt.xlabel('Attempt Number')
#     plt.ylabel('Memory Usage (MiB)')
#     plt.xticks(range(1, attempts + 1))
#     plt.grid()
#     plt.legend()
#     plt.tight_layout()
#     plt.show()

#     # Stop logging
#     logger.stop_logging()
# ======================================

# import solver
# import logger
# from time_tracker import TimeTracker
# from domains import initialize_domains as domains_init
# from simulated_anealing_solver import simulated_annealing
# import matplotlib.pyplot as plt
# import copy
# from memory_profiler import memory_usage

# def solve_with_memory_tracking(solver_function, *args, **kwargs):
#     # Track memory usage and execution time
#     timer = TimeTracker()
#     timer.start()
    
#     mem_usage = memory_usage((solver_function, args, kwargs), interval=0.1)
    
#     timer.stop()
#     elapsed_time = timer.elapsed_time()
    
#     return elapsed_time, max(mem_usage)  # Return time taken and max memory usage

# if __name__ == "__main__":
#     logger.start_logging('solver.log')

#     sudoku_grid = [
#         [0, 0, 5, 3, 0, 0, 0, 0, 0],
#         [8, 0, 0, 0, 0, 0, 0, 2, 0],
#         [0, 7, 0, 0, 1, 0, 5, 0, 0],
#         [4, 0, 0, 0, 0, 5, 3, 0, 0],
#         [0, 1, 0, 7, 0, 0, 0, 0, 6],
#         [0, 0, 3, 0, 0, 0, 0, 0, 2],
#         [0, 6, 0, 0, 0, 0, 0, 8, 0],
#         [0, 0, 0, 0, 2, 0, 0, 0, 3],
#         [0, 0, 0, 5, 0, 0, 7, 4, 0]
#     ]

#     # Define a list of initial temperatures to test
#     initial_temperatures = [1000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1280000]
    
#     attempts = 5  # Number of attempts for each temperature

#     mem_sa = []  # List to store memory usage for simulated annealing

#     for initial_temp in initial_temperatures:
#         temp_mem_usage = []  # List to store memory usage for this temperature
        
#         for attempt in range(attempts):
#             print(f"Running Simulated Annealing with initial temperature {initial_temp} (Attempt {attempt + 1})")
            
#             # Create deep copy of the grid for Simulated Annealing
#             current_sudoku_grid_sa = copy.deepcopy(sudoku_grid)

#             # Run Simulated Annealing Solver
#             _, max_mem_sa = solve_with_memory_tracking(
#                 simulated_annealing, current_sudoku_grid_sa, initial_temp=initial_temp, cooling_rate=0.999
#             )
#             temp_mem_usage.append(max_mem_sa)

#         mem_sa.append(temp_mem_usage)  # Append the memory usage for this temperature

#     # Output all memory usage for each temperature
#     print("\nMemory Usage (MiB) for different initial temperatures:")
#     for i, temp in enumerate(initial_temperatures):
#         avg_mem = sum(mem_sa[i]) / attempts
#         print(f"Initial Temp {temp}: Avg Memory Usage: {avg_mem:.2f} MiB")

#     # Plotting memory usage results
#     plt.figure(figsize=(10, 6))
#     for i, temp in enumerate(initial_temperatures):
#         plt.plot(range(1, attempts + 1), mem_sa[i], marker='o', label=f'Initial Temp: {temp}')
    
#     plt.title('Memory Usage of Simulated Annealing with Different Initial Temperatures')
#     plt.xlabel('Attempt Number')
#     plt.ylabel('Memory Usage (MiB)')
#     plt.xticks(range(1, attempts + 1))
#     plt.grid()
#     plt.legend()
#     plt.tight_layout()
#     plt.show()

#     # Stop logging
#     logger.stop_logging()

# --------------------------
# import solver
# import logger
# from time_tracker import TimeTracker
# from domains import initialize_domains as domains_init
# import copy  # Import copy for deep copying
# import matplotlib.pyplot as plt  # Import matplotlib for plotting
# from memory_profiler import memory_usage
# import gc  # Import garbage collection module


# def solve_with_memory_tracking(solver_function, *args, **kwargs):
#     # Track memory usage and execution time
#     timer = TimeTracker()
#     timer.start()
    
#     mem_usage = memory_usage((solver_function, args, kwargs), interval=0.1)
    
#     timer.stop()
#     elapsed_time = timer.elapsed_time()
    
#     return elapsed_time, max(mem_usage)  # Return time taken and max memory usage


# if __name__ == "__main__":
#     logger.start_logging('solver.log')

#     sudoku_grid = [
#           [8, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 3, 6, 0, 0, 0, 0, 0],
#     [0, 7, 0, 0, 9, 0, 2, 0, 0],
#     [0, 5, 0, 0, 0, 7, 0, 0, 0],
#     [0, 0, 0, 0, 4, 5, 7, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 3, 0],
#     [0, 0, 1, 0, 0, 0, 0, 6, 8],
#     [0, 0, 8, 5, 0, 0, 0, 1, 0],
#     [0, 9, 0, 0, 0, 0, 4, 0, 0]
#     ]

#     # Initialize domains
#     domains = domains_init(sudoku_grid)

#     times_backtracking_fc = []  # List to store times for backtracking solver with forward checking
#     mem_backtracking_fc = []  # List to store memory usage for backtracking with forward checking

#     attempts = 10  # Number of attempts for backtracking with forward checking

#     for attempt in range(attempts):
#         print(f"Attempt {attempt + 1}")

#         # Create deep copies of the grid and domains for each attempt
#         current_sudoku_grid_fc = copy.deepcopy(sudoku_grid)
#         domains_fc = domains_init(current_sudoku_grid_fc)

#         # Run Backtracking Solver with Forward Checking
#         elapsed_backtracking_fc, max_mem_backtracking_fc = solve_with_memory_tracking(
#             solver.solve_sudoku, current_sudoku_grid_fc, domains_fc, False, 0, False
#         )
#         times_backtracking_fc.append(elapsed_backtracking_fc)
#         mem_backtracking_fc.append(max_mem_backtracking_fc)

#         # Cleanup for backtracking with forward checking
#         del current_sudoku_grid_fc
#         del domains_fc
#         gc.collect()  # Force garbage collection

#     # Output all memory usage for each attempt
#     print("\nMemory Usage (MiB) for Backtracking with Forward Checking:")
#     for i in range(attempts):
#         print(f"Attempt {i + 1}: Backtracking FC: {mem_backtracking_fc[i]:.2f}")

#     # Plotting memory usage results
#     plt.figure(figsize=(10, 6))
#     plt.plot(range(1, attempts + 1), mem_backtracking_fc, marker='o', color='green', label='Backtracking with FC')
#     plt.title('Memory Usage of Backtracking Solver with Forward Checking')
#     plt.xlabel('Attempt Number')
#     plt.ylabel('Memory Usage (MiB)')
#     plt.xticks(range(1, attempts + 1))
#     plt.grid()
#     plt.legend()
#     plt.tight_layout()
#     plt.show()

#     # Stop logging
#     logger.stop_logging()
