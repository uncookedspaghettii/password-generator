import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

auto_generate_job = None  # track auto-generation

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for length.")
        return

    chars = ""
    if use_letters.get():
        chars += string.ascii_letters
    if use_digits.get():
        chars += string.digits
    if use_specials.get():
        chars += string.punctuation

    if not chars:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    password = "".join(random.choice(chars) for _ in range(length))
    password_var.set(password)

# Ultra-fast auto-generate
def start_auto_generate():
    global auto_generate_job
    generate_password()
    auto_generate_job = root.after(1, start_auto_generate)  # 1 millisecond delay

# Stop auto-generation
def stop_auto_generate():
    global auto_generate_job
    if auto_generate_job:
        root.after_cancel(auto_generate_job)
        auto_generate_job = None

# Copy password
def copy_password():
    if password_var.get():
        pyperclip.copy(password_var.get())
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("Ultra-Fast Password Generator")
root.geometry("420x360")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="🔑 Ultra-Fast Password Generator", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Length
length_frame = tk.Frame(root)
length_frame.pack(pady=5)
tk.Label(length_frame, text="Password Length:", font=("Arial", 11)).pack(side=tk.LEFT)
length_entry = tk.Entry(length_frame, width=5, font=("Arial", 11))
length_entry.pack(side=tk.LEFT, padx=5)
length_entry.insert(0, "12")

# Options
use_letters = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_specials = tk.BooleanVar(value=True)

options_frame = tk.Frame(root)
options_frame.pack(pady=5)
tk.Checkbutton(options_frame, text="Include Letters (A-Z, a-z)", variable=use_letters).pack(anchor="w")
tk.Checkbutton(options_frame, text="Include Digits (0-9)", variable=use_digits).pack(anchor="w")
tk.Checkbutton(options_frame, text="Include Special Characters (!@#$...)", variable=use_specials).pack(anchor="w")

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

generate_btn = tk.Button(btn_frame, text="Generate Once", font=("Arial", 11, "bold"), command=generate_password)
generate_btn.grid(row=0, column=0, padx=5)

auto_btn = tk.Button(btn_frame, text="Start Ultra-Fast Generate", font=("Arial", 11, "bold"), command=start_auto_generate)
auto_btn.grid(row=0, column=1, padx=5)

stop_btn = tk.Button(btn_frame, text="Stop", font=("Arial", 11, "bold"), command=stop_auto_generate)
stop_btn.grid(row=0, column=2, padx=5)

# Output
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=35, justify="center")
password_entry.pack(pady=10)

# Copy button
copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_password)
copy_btn.pack(pady=5)

# Run app
root.mainloop()
