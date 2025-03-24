import tkinter as tk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk







# Function to display the main screen
def show_main_screen(root):
    # Create the main screen window
    main_screen = tk.Toplevel(root)
    main_screen.title("Budget App - Main Screen")
    main_screen.geometry('540x600')
    main_screen.configure(bg='#333333')

    frame = tk.Frame(main_screen, bg="#333333")

    # Load logo image for the main screen
    img = Image.open("logo.png")
    img = img.resize((400, 200))
    bg_image = ImageTk.PhotoImage(img)
    background_label = tk.Label(frame, image=bg_image, bg="#333333")
    background_label.image = bg_image  # Keep a reference to prevent garbage collection


    # Widget placements
    background_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=10)
    frame.pack()

    main_screen.protocol("WM_DELETE_WINDOW", lambda: close_main_screen(main_screen))

    # Function to close the main screen and return to login screen
    def close_main_screen(screen):
        screen.destroy()
        root.deiconify()  # Show the login screen again

# Start the application with login screen
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide login screen initially
    from login import login  # Importing login function after Tk root is created
    login()