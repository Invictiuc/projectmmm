import tkinter as tk
from tkinter import ttk
from signals import compute_signal as compute_signal_func

def update_scales(event=None):
    try:
        new_length = param_frame.winfo_width() - 300
        for child in param_frame.winfo_children():
            if isinstance(child, tk.Scale):
                child.config(length=max(200, new_length))
    except:
        pass

def validate_float(P):
    if P == "":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False

def compute_signal():
    try:
        a0 = float(entry_a0.get())
        a1 = float(entry_a1.get())
        b0 = float(entry_b0.get())
        b1 = float(entry_b1.get())
        b2 = float(entry_b2.get())
        kp = float(entry_kp.get())
        Tf = float(entry_Tf.get())
        kd = float(entry_kd.get())
        A = float(entry_A.get())  # Amplituda
        T = float(entry_T.get())  # Czas trwania / okres
        w = float(entry_w.get())  # Częstotliwość
        signal_choice = signal_var.get().lower()

        result_str = compute_signal_func(a0, a1, b0, b1, b2, kp, Tf, kd, A, T, w, signal_choice)
        result.set(result_str)
    except ValueError:
        result.set("Please enter valid numbers for all parameters.")

# Create main window
root = tk.Tk()
root.title("Signal Calculator")

# Set window to 1/2 width and 3/4 height of screen for better visibility
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = screen_width // 2
height = screen_height * 3 // 4
root.geometry(f"{width}x{height}")

root.resizable(True, True)

vcmd = (root.register(validate_float), '%P')

# Main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Variables
entry_a0 = tk.DoubleVar(value=1)
entry_a1 = tk.DoubleVar(value=1)
entry_b0 = tk.DoubleVar(value=1)
entry_b1 = tk.DoubleVar(value=1)
entry_b2 = tk.DoubleVar(value=1)
entry_kp = tk.DoubleVar(value=1)
entry_Tf = tk.DoubleVar(value=1)
entry_kd = tk.DoubleVar(value=1)
entry_A = tk.DoubleVar(value=1)
entry_T = tk.DoubleVar(value=5)
entry_w = tk.DoubleVar(value=1)
signal_var = tk.StringVar(value="square")
result = tk.StringVar()

# Parameters frame
param_frame = ttk.Frame(main_frame, padding="5")
param_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
param_frame.columnconfigure(2, weight=1)

params = [
    ("a0", entry_a0),
    ("a1", entry_a1),
    ("b0", entry_b0),
    ("b1", entry_b1),
    ("b2", entry_b2),
    ("kp", entry_kp),
    ("Tf", entry_Tf),
    ("kd", entry_kd),
    ("A (amplitude)", entry_A),
    ("T (time/period)", entry_T),
    ("w (frequency)", entry_w),
]

# Calculate scale length based on window width
scale_length = max(200, width - 300)

# Create labels, entries, and scales in a loop
for i, (name, var) in enumerate(params):
    ttk.Label(param_frame, text=f"{name}:").grid(row=i, column=0, sticky=tk.W, padx=5, pady=2)
    ttk.Entry(param_frame, textvariable=var, validate="key", validatecommand=vcmd).grid(row=i, column=1, padx=5, pady=2)
    tk.Scale(param_frame, from_=0.1, to=50, resolution=0.1, orient=tk.HORIZONTAL, variable=var, length=scale_length).grid(row=i, column=2, sticky=(tk.W, tk.E), padx=5, pady=2)

# Bind resize event to update scales
root.bind('<Configure>', update_scales)

# Controls frame
control_frame = ttk.Frame(main_frame, padding="5")
control_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

ttk.Label(control_frame, text="Signal type:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
ttk.Combobox(control_frame, textvariable=signal_var, values=["square", "sin", "triangle"], state="readonly").grid(row=0, column=1, padx=5, pady=2)
ttk.Button(control_frame, text="Compute", command=compute_signal).grid(row=0, column=2, padx=5, pady=2)

# Result frame
result_frame = ttk.Frame(main_frame, padding="5")
result_frame.grid(row=2, column=0, sticky=(tk.W, tk.E))

ttk.Label(result_frame, textvariable=result, wraplength=800).grid(row=0, column=0, padx=5, pady=2)

root.mainloop()