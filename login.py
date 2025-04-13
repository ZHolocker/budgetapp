import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from main import show_main_screen
import re

# Create login window
root = tk.Tk()
root.title("Login form")
root.geometry('540x600')
root.configure(bg='#333333')

frame = tk.Frame(root, bg="#333333")

# Load logo image
img = Image.open("logo.png")  # Make sure the logo is in the same directory as the script
img = img.resize((400, 200))  # Adjust the size as needed
bg_image = ImageTk.PhotoImage(img)

# Function to login
def login(root):
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Login Success", "Welcome to the Budget App!")
            show_main_screen(root)  # Call the function to show the main screen
            root.withdraw()  # Hide login screen
        else:
            messagebox.showerror("Login Error", "Invalid username or password!")
        
        connection.close()
    else:
        messagebox.showerror("Input Error", "Please enter both username and password.")

# Function for new user registration
def new_user():
    username = username_entry.get()
    password = password_entry.get()
    
    # Module 4 security additions to enforce a minimum password length and use of special characters
    # industry standard says 6-8 characters minimum is good, since this is a simple app, I chose 6 characters
    #I put the return at the end to end the function if the user's password doesn't meet the requirements
    if len(password) < 6 or not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        messagebox.showerror("Password Error", "Password must be at least 6 characters long and contain at least one special character.")
        return

    if username and password:
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
        
        # Check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        if cursor.fetchone():
            messagebox.showerror("User Error", "Username already exists!")
        else:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            connection.commit()
            messagebox.showinfo("Registration Success", "New user created!")
        
        connection.close()
    else:
        messagebox.showerror("Input Error", "Please enter both username and password.")

# Create widgets
background_label = tk.Label(frame, image=bg_image, bg="#333333")
login_label = tk.Label(frame, text="Login", bg="#333333", fg="#FFFFFF", font=("Arial", 30))
username_label = tk.Label(frame, text="Username", bg="#333333", fg="#FFFFFF", font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 16))
password_label = tk.Label(frame, text="Password", bg="#333333", fg="#FFFFFF", font=("Arial", 16))
password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
login_button = tk.Button(frame, text="Login", bg="lightblue", font=("Arial", 16), command=lambda: login(root))
create_user_button = tk.Button(frame, text="Create New User", bg="lightgreen", font=("Arial", 16), command=new_user)

# Widget placements
background_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=10)
login_label.grid(row=1, column=0, columnspan=2, sticky="news", pady=10)
username_label.grid(row=2, column=0)
username_entry.grid(row=2, column=1, pady=20)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1, pady=20)
login_button.grid(row=4, column=0, columnspan=2, pady=30)
create_user_button.grid(row=5, column=0, columnspan=2, pady=10)

# Frame packing
frame.pack()

root.mainloop()