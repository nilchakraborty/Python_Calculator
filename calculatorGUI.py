import tkinter as tk # tkinter is the standard GUI library for Python

class Calculator:
    def __init__(self, master): # master is the root window
        self.master = master
        master.title("Calculator")
        master.config(bg="#000000") # Set background color of master to black

        # Create the entry widget for displaying results
        self.entry = tk.Entry(master, width=12, borderwidth=5, font=('Arial', 24))
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Create buttons for digits and operations
        buttons = [
            '1', '2', '3', '+',
            '4', '5', '6', '-',
            '7', '8', '9', '*',
            '.', '0', '=', '/', 
            '(', ')'
        ]

        # Initialize row and column indices
        row, col = 1, 0

        # Create the buttons and add them to the grid
        for button in buttons:
            if button == '=':
                command = lambda text=button: self.button_click(text) # Lambda function to handle button clicks
                bg_color = "#ffa500"
            else:
                command = lambda text=button: self.button_click(text)
                bg_color = "#ffffff"
            tk.Button(master, text=button, width=5, height=3, command=command, font=('Arial', 12), bg=bg_color).grid(row=row, column=col) # grid() is a method of the grid layout manager
            col += 1
            if col > 3:
                col = 0
                row += 1
        # Create a Clear button
        clear_button = tk.Button(master, text='C', width=12, height=3, command=self.clear, font=('Arial', 12), bg='#0000ff')
        clear_button.grid(row=5, column=2, columnspan=2)

    def button_click(self, text):
        """Handle button clicks and update the entry widget."""
        if text == '=':
            try:
                result = str(eval(self.entry.get())) # eval() evaluates a string as a Python expression
                self.entry.delete(0, tk.END) # Delete the contents of the entry widget
                self.entry.insert(0, result) # Insert the result into the entry widget
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, 'Error')
        else:
            self.entry.insert(tk.END, text)

    def clear(self):
        """Clear the entry widget."""
        self.entry.delete(0, tk.END)

root = tk.Tk() # Create the root window
calculator = Calculator(root) # Create an instance of the Calculator class
root.mainloop() # Start the event loop