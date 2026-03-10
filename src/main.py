import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk() #hide main window
root.withdraw()   

def get_user_data():
    dialog = tk.Toplevel(root)
    dialog.title("Enter Data")
    
    def validate_numeric(text):
        if text == "":
            return True
        try:
            float(text)
            return True
        except ValueError:
            return False
    
    def validate_alpha(text):
        return all(c.isalpha() or c.isspace() for c in text) or text == ""
    
    vcmd_numeric = (dialog.register(validate_numeric), '%P')
    vcmd_alpha = (dialog.register(validate_alpha), '%P')
    
    # Name field
    tk.Label(dialog, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(dialog, validate="key", validatecommand=vcmd_alpha)
    name_entry.grid(row=0, column=1)
    
    # a fields
    tk.Label(dialog, text="a[0]:").grid(row=1, column=0)
    a0_entry = tk.Entry(dialog, validate="key", validatecommand=vcmd_numeric)
    a0_entry.grid(row=1, column=1)
    tk.Label(dialog, text="a[1]:").grid(row=2, column=0)
    a1_entry = tk.Entry(dialog, validate="key", validatecommand=vcmd_numeric)
    a1_entry.grid(row=2, column=1)
    
    # b fields
    tk.Label(dialog, text="b[0]:").grid(row=3, column=0)
    b0_entry = tk.Entry(dialog, validate="key", validatecommand=vcmd_numeric)
    b0_entry.grid(row=3, column=1)
    tk.Label(dialog, text="b[1]:").grid(row=4, column=0)
    b1_entry = tk.Entry(dialog, validate="key", validatecommand=vcmd_numeric)
    b1_entry.grid(row=4, column=1)
    tk.Label(dialog, text="b[2]:").grid(row=5, column=0)
    b2_entry = tk.Entry(dialog, validate="key", validatecommand=vcmd_numeric)
    b2_entry.grid(row=5, column=1)
    
    # PD fields
    tk.Label(dialog, text="PD[0]:").grid(row=6, column=0)
    pd0_entry = tk.Entry(dialog, validate="key", validatecommand=vcmd_numeric)
    pd0_entry.grid(row=6, column=1)
    tk.Label(dialog, text="PD[1]:").grid(row=7, column=0)
    pd1_entry = tk.Entry(dialog, validate="key", validatecommand=vcmd_numeric)
    pd1_entry.grid(row=7, column=1)
    
    def submit():
        global user_input, a, b, PD
        user_input = name_entry.get()
        try:
            a = [float(a0_entry.get()), float(a1_entry.get())]
        except ValueError:
            a = [1, 1]
        try:
            b = [float(b0_entry.get()), float(b1_entry.get()), float(b2_entry.get())]
        except ValueError:
            b = [1, 1, 1]
        try:
            PD = [float(pd0_entry.get()), float(pd1_entry.get())]
        except ValueError:
            PD = [1, 1]
        dialog.destroy()
    
    tk.Button(dialog, text="Submit", command=submit).grid(row=8, column=0, columnspan=2)
    dialog.wait_window()

get_user_data()

if user_input:
    print(f"Hello, {user_input}!")
else:
    print("Cancelled or nothing entered.")


# Your variables a, b, PD...

print(f"Name retrieved: {user_input}") # Check in terminal if it works
print(f"Retrieved values: a={a}, b={b}, PD={PD}")
root.mainloop()
