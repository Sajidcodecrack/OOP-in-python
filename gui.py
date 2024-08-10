import tkinter as tk
import turtle
def button_click(symbol):
    current = entry.get()
    if current == 'Error':
        entry.delete(0, tk.END)
    if symbol == '=':
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, 'Error')
    elif symbol == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, symbol)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry widget
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button symbols
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Create and place buttons
row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=39, pady=20, command=lambda: button_click(button)).grid(row=row, column=col, columnspan=2)
        col += 2
    else:
        tk.Button(root, text=button, padx=40, pady=20, command=lambda b=button: button_click(b)).grid(row=row, column=col)
        col += 1
    if col > 3:
        col = 0
        row += 1

# Run the Tkinter event loop
root.mainloop()
