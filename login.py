import tkinter as tk
from tkinter import messagebox

def create_login_window():
    def login():
        username = entry_username.get()
        password = entry_password.get()
        # Simple validation
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Success", "Welcome to the budget app!")
        else:
            messagebox.showerror("Login Error", "Invalid username or password!")
    # Create the main window
    root = tk.Tk()
    root.title("Login Page")

    # Username and Password labels and entry fields
    tk.Label(root, text="Username:").pack(pady=5)
    entry_username = tk.Entry(root)
    entry_username.pack(pady=5)

    tk.Label(root, text="Password:").pack(pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)

    # Login Button, calling the login function when pressed
    login_button = tk.Button(root, text="Login", command=login)
    login_button.pack(pady=20)

    root.mainloop()


