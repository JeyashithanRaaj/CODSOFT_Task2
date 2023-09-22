import tkinter as tk
from tkinter import messagebox

def add():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result.set(num1 + num2)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def subtract():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result.set(num1 - num2)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def multiply():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result.set(num1 * num2)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero.")
        else:
            result.set(num1 / num2)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def add_digit(digit):
    current_text = entry_num1.get()
    if current_text == "0":
        entry_num1.delete(0, tk.END)
    entry_num1.insert(tk.END, str(digit))

def add_decimal():
    current_text = entry_num1.get()
    if '.' not in current_text:
        entry_num1.insert(tk.END, '.')

root = tk.Tk()
root.title("Simple Calculator")

frame = tk.Frame(root)
frame.pack(pady=10)

label_num1 = tk.Label(frame, text="Enter number 1:")
label_num1.grid(row=0, column=0, padx=10)

entry_num1 = tk.Entry(frame)
entry_num1.grid(row=0, column=1, padx=10)

label_num2 = tk.Label(frame, text="Enter number 2:")
label_num2.grid(row=1, column=0, padx=10)

entry_num2 = tk.Entry(frame)
entry_num2.grid(row=1, column=1, padx=10)

result = tk.StringVar()
result.set("Result will be displayed here")

label_result = tk.Label(frame, textvariable=result)
label_result.grid(row=2, columnspan=2, padx=10, pady=10)

add_button = tk.Button(frame, text="Add", command=add)
add_button.grid(row=3, column=0, padx=10)

subtract_button = tk.Button(frame, text="Subtract", command=subtract)
subtract_button.grid(row=3, column=1, padx=10)

multiply_button = tk.Button(frame, text="Multiply", command=multiply)
multiply_button.grid(row=4, column=0, padx=10)

divide_button = tk.Button(frame, text="Divide", command=divide)
divide_button.grid(row=4, column=1, padx=10)

for i in range(1, 10):
    button = tk.Button(frame, text=str(i), command=lambda i=i: add_digit(i))
    button.grid(row=(i - 1) // 3 + 5, column=(i - 1) % 3, padx=5, pady=5)

button_zero = tk.Button(frame, text="0", command=lambda: add_digit(0))
button_zero.grid(row=8, column=1, padx=5, pady=5)

button_decimal = tk.Button(frame, text=".", command=add_decimal)
button_decimal.grid(row=8, column=2, padx=5, pady=5)


root.mainloop()
