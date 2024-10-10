import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def hill_climbing(func, start, step_size, max_iterations):
    current_solution = start
    current_value = func(current_solution)
    history = [(current_solution, current_value)]

    for _ in range(max_iterations):
        # Generate neighbors
        neighbors = [current_solution + step_size, current_solution - step_size]
        
        # Evaluate neighbors
        neighbor_values = [func(neighbor) for neighbor in neighbors]
        
        # Find the best neighbor
        best_neighbor_index = np.argmax(neighbor_values)
        best_neighbor_value = neighbor_values[best_neighbor_index]
        
        # If the best neighbor is better than current, move to that neighbor
        if best_neighbor_value > current_value:
            current_solution = neighbors[best_neighbor_index]
            current_value = best_neighbor_value
            history.append((current_solution, current_value))
        else:
            break  # No better neighbor found

    return current_solution, current_value, history

def optimize():
    try:
        func_str = func_entry.get()
        start = float(start_entry.get())
        step_size = float(step_entry.get())
        max_iterations = int(iter_entry.get())

        # Convert the function string to a callable function
        func = eval("lambda x: " + func_str)

        solution, value, history = hill_climbing(func, start, step_size, max_iterations)

        # Display result
        result_label.config(text=f"Optimal Solution: {solution:.4f}, Value: {value:.4f}")

        # Plotting the history
        plt.figure(figsize=(10, 5))
        plt.plot(*zip(*history), marker='o')
        plt.title("Hill Climbing Optimization Process")
        plt.xlabel("Solution")
        plt.ylabel("Function Value")
        plt.grid()
        plt.axhline(y=value, color='r', linestyle='--', label='Optimal Value')
        plt.axvline(x=solution, color='g', linestyle='--', label='Optimal Solution')
        plt.legend()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create GUI
root = tk.Tk()
root.title("Hill Climbing Algorithm GUI")

# Input fields
tk.Label(root, text="Function (in terms of x):").grid(row=0, column=0)
func_entry = tk.Entry(root)
func_entry.grid(row=0, column=1)

tk.Label(root, text="Start Point:").grid(row=1, column=0)
start_entry = tk.Entry(root)
start_entry.grid(row=1, column=1)

tk.Label(root, text="Step Size:").grid(row=2, column=0)
step_entry = tk.Entry(root)
step_entry.grid(row=2, column=1)

tk.Label(root, text="Max Iterations:").grid(row=3, column=0)
iter_entry = tk.Entry(root)
iter_entry.grid(row=3, column=1)

# Optimize button
optimize_button = tk.Button(root, text="Optimize", command=optimize)
optimize_button.grid(row=4, columnspan=2)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=5, columnspan=2)

root.mainloop()
