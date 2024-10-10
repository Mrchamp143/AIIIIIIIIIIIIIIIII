import tkinter as tk
from tkinter import messagebox

class AlphaBetaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Alpha-Beta Pruning Visualization")
        
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()

        self.btn_run = tk.Button(root, text="Run Alpha-Beta Search", command=self.run_alpha_beta)
        self.btn_run.pack()

        self.label = tk.Label(root, text="Enter node values (comma-separated):")
        self.label.pack()

        self.node_input = tk.Entry(root)
        self.node_input.pack()

        self.tree_depth = 3
        self.node_values = []

    def run_alpha_beta(self):
        input_values = self.node_input.get()
        self.node_values = list(map(int, input_values.split(',')))
        
        if len(self.node_values) != 2 ** self.tree_depth:
            messagebox.showerror("Error", "Please enter values for exactly {} nodes.".format(2 ** self.tree_depth))
            return

        self.canvas.delete("all")
        best_value = self.alpha_beta(0, 0, float('-inf'), float('inf'))
        messagebox.showinfo("Result", f"Optimal Value: {best_value}")

    def alpha_beta(self, depth, index, alpha, beta):
        if depth == self.tree_depth:
            return self.node_values[index]
        
        if depth % 2 == 0:  # Maximizing player
            max_eval = float('-inf')
            for i in range(2):  # Two children
                eval = self.alpha_beta(depth + 1, index * 2 + i, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:  # Minimizing player
            min_eval = float('inf')
            for i in range(2):  # Two children
                eval = self.alpha_beta(depth + 1, index * 2 + i, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

if __name__ == "__main__":
    root = tk.Tk()
    app = AlphaBetaGUI(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox

class AlphaBetaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Alpha-Beta Pruning Visualization")
        
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()

        self.btn_run = tk.Button(root, text="Run Alpha-Beta Search", command=self.run_alpha_beta)
        self.btn_run.pack()

        self.label = tk.Label(root, text="Enter node values (comma-separated):")
        self.label.pack()

        self.node_input = tk.Entry(root)
        self.node_input.pack()

        self.tree_depth = 3
        self.node_values = []

    def run_alpha_beta(self):
        input_values = self.node_input.get()
        self.node_values = list(map(int, input_values.split(',')))
        
        if len(self.node_values) != 2 ** self.tree_depth:
            messagebox.showerror("Error", "Please enter values for exactly {} nodes.".format(2 ** self.tree_depth))
            return

        self.canvas.delete("all")
        best_value = self.alpha_beta(0, 0, float('-inf'), float('inf'))
        messagebox.showinfo("Result", f"Optimal Value: {best_value}")

    def alpha_beta(self, depth, index, alpha, beta):
        if depth == self.tree_depth:
            return self.node_values[index]
        
        if depth % 2 == 0:  # Maximizing player
            max_eval = float('-inf')
            for i in range(2):  # Two children
                eval = self.alpha_beta(depth + 1, index * 2 + i, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:  # Minimizing player
            min_eval = float('inf')
            for i in range(2):  # Two children
                eval = self.alpha_beta(depth + 1, index * 2 + i, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

if __name__ == "__main__":
    root = tk.Tk()
    app = AlphaBetaGUI(root)
    root.mainloop()
