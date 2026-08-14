import tkinter as tk
from tkinter import messagebox, ttk
import random
import string


def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Invalid Input", "Password length must be a positive number.")
            return
        if length > 128:
            messagebox.showerror("Invalid Input", "Please choose a length of 128 or less.")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length.")
        return

    difficulty = difficulty_var.get()

    # Define character pools based on difficulty
    if difficulty == "Easy":
        # Letters only (upper + lower)
        char_pool = string.ascii_letters
    elif difficulty == "Medium":
        # Letters + numbers
        char_pool = string.ascii_letters + string.digits
    elif difficulty == "Hard":
        # Letters + numbers + symbols
        char_pool = string.ascii_letters + string.digits + string.punctuation
    else:
        messagebox.showerror("Error", "Please select a difficulty level.")
        return

    if length < 4 and difficulty != "Easy":
        messagebox.showwarning("Weak Length", "Consider a longer password for better security.")

    # Generate random password using random.choice in a loop (random string concept)
    password = ''.join(random.choice(char_pool) for _ in range(length))

    password_var.set(password)
    strength_label.config(text=f"Difficulty: {difficulty}")


def copy_to_clipboard():
    password = password_var.get()
    if not password:
        messagebox.showwarning("Nothing to Copy", "Generate a password first!")
        return
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()  # Keeps clipboard content after window closes
    messagebox.showinfo("Copied", "Password copied to clipboard!")


# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x320")
root.resizable(False, False)

title_label = tk.Label(root, text="🔐 Password Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=15)

# Length input
length_frame = tk.Frame(root)
length_frame.pack(pady=5)

tk.Label(length_frame, text="Password Length:", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
length_entry = tk.Entry(length_frame, width=10, font=("Arial", 11))
length_entry.pack(side=tk.LEFT)
length_entry.insert(0, "12")

# Difficulty selection
difficulty_frame = tk.Frame(root)
difficulty_frame.pack(pady=15)

tk.Label(difficulty_frame, text="Select Difficulty:", font=("Arial", 11)).pack()

difficulty_var = tk.StringVar(value="Medium")
difficulty_options = ["Easy", "Medium", "Hard"]

for option in difficulty_options:
    tk.Radiobutton(
        difficulty_frame,
        text=option,
        variable=difficulty_var,
        value=option,
        font=("Arial", 10)
    ).pack(anchor=tk.W)

# Generate button
generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=5
)
generate_btn.pack(pady=15)

# Display generated password
password_var = tk.StringVar()
password_display = tk.Entry(
    root,
    textvariable=password_var,
    font=("Consolas", 13),
    justify="center",
    state="readonly",
    width=30
)
password_display.pack(pady=5)

strength_label = tk.Label(root, text="", font=("Arial", 9), fg="gray")
strength_label.pack()

# Copy button
copy_btn = tk.Button(
    root,
    text="Copy to Clipboard",
    command=copy_to_clipboard,
    bg="#2196F3",
    fg="white",
    font=("Arial", 10),
    padx=10,
    pady=3
)
copy_btn.pack(pady=15)

root.mainloop()