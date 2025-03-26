import tkinter as tk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk

# Function to add budget entry
def add_budget(main_screen):
    def save_budget():
        category = category_entry.get()
        amount = amount_entry.get()
        date = date_entry.get()

        if category and amount and date:
            connection = sqlite3.connect("budget.db")
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS budget_entries (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, amount TEXT, date TEXT)")
            cursor.execute("INSERT INTO budget_entries (category, amount, date) VALUES (?, ?, ?)", (category, amount, date))
            connection.commit()
            connection.close()
            messagebox.showinfo("Success", "Item added successfully!")
            new_budget_window.destroy()

        else:
            messagebox.showerror("Input Error", "All fields must be filled out!")

    # Create a new window to add a budget entry
    new_budget_window = tk.Toplevel(main_screen)
    new_budget_window.title("Add Budget Entry")
    new_budget_window.geometry('540x400')
    new_budget_window.configure(bg='#333333')

    # Load logo image for the add entry window
    img = Image.open("logo.png")
    img = img.resize((400, 200))
    bg_image = ImageTk.PhotoImage(img)
    background_label = tk.Label(new_budget_window, image=bg_image, bg="#333333")
    background_label.image = bg_image  # Keep a reference to prevent garbage collection

    category_label = tk.Label(new_budget_window, text="Category", font=("Arial", 14), bg="#333333", fg="#FFFFFF")
    category_entry = tk.Entry(new_budget_window, font=("Arial", 14))
    amount_label = tk.Label(new_budget_window, text="Amount", font=("Arial", 14), bg="#333333", fg="#FFFFFF")
    amount_entry = tk.Entry(new_budget_window, font=("Arial", 14))
    date_label = tk.Label(new_budget_window, text="Date", font=("Arial", 14), bg="#333333", fg="#FFFFFF")
    date_entry = tk.Entry(new_budget_window, font=("Arial", 14))

    save_button = tk.Button(new_budget_window, text="Save", font=("Arial", 14), command=save_budget, bg="lightblue")
    cancel_button = tk.Button(new_budget_window, text="Cancel", font=("Arial", 14), command=new_budget_window.destroy, bg="lightcoral")

    # Widget placements
    background_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=10)
    category_label.grid(row=1, column=0, pady=5)
    category_entry.grid(row=1, column=1, pady=5)
    amount_label.grid(row=2, column=0, pady=5)
    amount_entry.grid(row=2, column=1, pady=5)
    date_label.grid(row=3, column=0, pady=5)
    date_entry.grid(row=3, column=1, pady=5)
    save_button.grid(row=4, column=0, columnspan=2, pady=20)
    cancel_button.grid(row=5, column=0, columnspan=2, pady=10)

# Function to update budget entry
def update_budget(main_screen):
    def save_update():
        category = category_entry.get()
        amount = amount_entry.get()
        date = date_entry.get()

        if category and amount and date:
            connection = sqlite3.connect("budget.db")
            cursor = connection.cursor()
            cursor.execute("UPDATE budget_entries SET category=?, amount=?, date=? WHERE id=?",
                           (category, amount, date, entry_id))
            connection.commit()
            connection.close()
            messagebox.showinfo("Success", "Item updated successfully!")
            update_budget_window.destroy()

        else:
            messagebox.showerror("Input Error", "All fields must be filled out!")

    # Create a new window to update a budget entry
    update_budget_window = tk.Toplevel(main_screen)
    update_budget_window.title("Update Budget Entry")
    update_budget_window.geometry('540x400')
    update_budget_window.configure(bg='#333333')

    # Get the selected entry ID for update
    entry_id = int(entry_id_entry.get())

    category_label = tk.Label(update_budget_window, text="Category", font=("Arial", 14), bg="#333333", fg="#FFFFFF")
    category_entry = tk.Entry(update_budget_window, font=("Arial", 14))
    amount_label = tk.Label(update_budget_window, text="Amount", font=("Arial", 14), bg="#333333", fg="#FFFFFF")
    amount_entry = tk.Entry(update_budget_window, font=("Arial", 14))
    date_label = tk.Label(update_budget_window, text="Date", font=("Arial", 14), bg="#333333", fg="#FFFFFF")
    date_entry = tk.Entry(update_budget_window, font=("Arial", 14))

    save_button = tk.Button(update_budget_window, text="Save", font=("Arial", 14), command=save_update, bg="lightblue")
    cancel_button = tk.Button(update_budget_window, text="Cancel", font=("Arial", 14), command=update_budget_window.destroy, bg="lightcoral")

    category_label.grid(row=0, column=0, pady=5)
    category_entry.grid(row=0, column=1, pady=5)
    amount_label.grid(row=1, column=0, pady=5)
    amount_entry.grid(row=1, column=1, pady=5)
    date_label.grid(row=2, column=0, pady=5)
    date_entry.grid(row=2, column=1, pady=5)
    save_button.grid(row=3, column=0, columnspan=2, pady=20)
    cancel_button.grid(row=4, column=0, columnspan=2, pady=10)



# Function to display all budget entries
def display_all_entries(main_screen):
    connection = sqlite3.connect("budget.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM budget_entries")
    rows = cursor.fetchall()

    if rows:
        display_window = tk.Toplevel(main_screen)
        display_window.title("All Budget Entries")
        display_window.geometry('540x400')
        display_window.configure(bg='#333333')

        display_text = tk.Text(display_window, wrap=tk.WORD, font=("Arial", 14))
        display_text.pack(expand=True, fill=tk.BOTH)

        for row in rows:
            display_text.insert(tk.END, f"ID: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Date: {row[3]}\n")

        connection.close()
    else:
        messagebox.showinfo("No Entries", "No budget entries found.")

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

    # Create buttons with their respective functions
    add_button = tk.Button(frame, text="Add Entry", bg="lightblue", font=("Arial", 16), command=lambda: add_budget(main_screen))
    update_button = tk.Button(frame, text="Update Entry", bg="lightgreen", font=("Arial", 16), command=lambda: update_budget(main_screen))
    display_button = tk.Button(frame, text="Display All Entries", bg="lightyellow", font=("Arial", 16), command=lambda: display_all_entries(main_screen))

    # Widget placements
    background_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=10)
    add_button.grid(row=1, column=0, columnspan=2, pady=10)
    update_button.grid(row=2, column=0, columnspan=2, pady=10)
    display_button.grid(row=4, column=0, columnspan=2, pady=10)

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
