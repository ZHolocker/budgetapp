import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

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
    #img = Image.open(r"C:\Users\MrHol\OneDrive\Desktop\budgetapp1.2\logo.png")
    #img = img.resize((400, 200))
    #bg_image = ImageTk.PhotoImage(img)
    #background_label = tk.Label(new_budget_window, image=bg_image, bg="#333333")
    #background_label.image = bg_image  # Keep a reference to prevent garbage collection

    category_label = tk.Label(new_budget_window, text="Category", font=("Arial", 14), bg="#333333", fg="#FFFFFF")
    category_entry = tk.Entry(new_budget_window, font=("Arial", 14))
    amount_label = tk.Label(new_budget_window, text="Amount", font=("Arial", 14), bg="#333333", fg="#FFFFFF")
    amount_entry = tk.Entry(new_budget_window, font=("Arial", 14))
    date_label = tk.Label(new_budget_window, text="Date", font=("Arial", 14), bg="#333333", fg="#FFFFFF")
    date_entry = tk.Entry(new_budget_window, font=("Arial", 14))

    save_button = tk.Button(new_budget_window, text="Save", font=("Arial", 14), command=save_budget, bg="lightblue")
    cancel_button = tk.Button(new_budget_window, text="Cancel", font=("Arial", 14), command=new_budget_window.destroy, bg="lightcoral")

    # Widget placements
    #background_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=10)
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
        entry_id = entry_id_entry.get()
        category = category_entry.get()
        amount = amount_entry.get()
        date = date_entry.get()

        if category and amount and date and entry_id:
            connection = sqlite3.connect("budget.db")
            cursor = connection.cursor()
            cursor.execute("UPDATE budget_entries SET category=?, amount=?, date=? WHERE id=?", (category, amount, date, entry_id))
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

    # Create widgets for entry ID input
    entry_id_label = tk.Label(update_budget_window, text="Entry ID", font=("Arial", 14), bg="#333333", fg="#FFFFFF")
    entry_id_entry = tk.Entry(update_budget_window, font=("Arial", 14))

    # Create widgets for category, amount, and date inputs
    category_label = tk.Label(update_budget_window, text="Category", font=("Arial", 14), bg="#333333", fg="#FFFFFF")
    category_entry = tk.Entry(update_budget_window, font=("Arial", 14))
    amount_label = tk.Label(update_budget_window, text="Amount", font=("Arial", 14), bg="#333333", fg="#FFFFFF")
    amount_entry = tk.Entry(update_budget_window, font=("Arial", 14))
    date_label = tk.Label(update_budget_window, text="Date", font=("Arial", 14), bg="#333333", fg="#FFFFFF")
    date_entry = tk.Entry(update_budget_window, font=("Arial", 14))

    # Button for saving the update
    save_button = tk.Button(update_budget_window, text="Save", font=("Arial", 14), command=save_update, bg="lightblue")
    cancel_button = tk.Button(update_budget_window, text="Cancel", font=("Arial", 14), command=update_budget_window.destroy, bg="lightcoral")

    # Positioning widgets
    entry_id_label.grid(row=0, column=0, pady=5)
    entry_id_entry.grid(row=0, column=1, pady=5)
    category_label.grid(row=1, column=0, pady=5)
    category_entry.grid(row=1, column=1, pady=5)
    amount_label.grid(row=2, column=0, pady=5)
    amount_entry.grid(row=2, column=1, pady=5)
    date_label.grid(row=3, column=0, pady=5)
    date_entry.grid(row=3, column=1, pady=5)
    save_button.grid(row=4, column=0, columnspan=2, pady=20)
    cancel_button.grid(row=5, column=0, columnspan=2, pady=10)

    # Function to populate fields if an entry ID is provided
    def populate_fields(entry_id):
        connection = sqlite3.connect("budget.db")
        cursor = connection.cursor()
        cursor.execute("SELECT category, amount, date FROM budget_entries WHERE id=?", (entry_id,))
        result = cursor.fetchone()
        if result:
            category_entry.insert(0, result[0])
            amount_entry.insert(0, result[1])
            date_entry.insert(0, result[2])
        connection.close()

    # Trigger the population of the fields when an entry ID is entered
    def on_entry_id_entered(event=None):
        entry_id = entry_id_entry.get()
        if entry_id:
            populate_fields(entry_id)

    # Bind the Enter key to trigger field population
    entry_id_entry.bind("<Return>", on_entry_id_entered)

# Function to delete budget entry
def delete_budget(main_screen):
    def confirm_delete():
        entry_id = entry_id_entry.get()

        if entry_id:
            connection = sqlite3.connect("budget.db")
            cursor = connection.cursor()
            cursor.execute("DELETE FROM budget_entries WHERE id=?", (entry_id,))
            connection.commit()
            connection.close()
            messagebox.showinfo("Success", f"Entry with ID {entry_id} deleted successfully!")
            delete_budget_window.destroy()

        else:
            messagebox.showerror("Input Error", "Please enter an entry ID to delete!")

    # Create a new window to delete a budget entry
    delete_budget_window = tk.Toplevel(main_screen)
    delete_budget_window.title("Delete Budget Entry")
    delete_budget_window.geometry('540x400')
    delete_budget_window.configure(bg='#333333')

    entry_id_label = tk.Label(delete_budget_window, text="Entry ID", font=("Arial", 14), bg="#333333", fg="#FFFFFF")
    entry_id_entry = tk.Entry(delete_budget_window, font=("Arial", 14))

    delete_button = tk.Button(delete_budget_window, text="Delete", font=("Arial", 14), command=confirm_delete, bg="lightcoral")
    cancel_button = tk.Button(delete_budget_window, text="Cancel", font=("Arial", 14), command=delete_budget_window.destroy, bg="lightblue")

    entry_id_label.grid(row=0, column=0, pady=5)
    entry_id_entry.grid(row=0, column=1, pady=5)
    delete_button.grid(row=1, column=0, columnspan=2, pady=20)
    cancel_button.grid(row=2, column=0, columnspan=2, pady=10)

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

#generate report and generate_pie_chart functions

# Function to generate a summary report and pie chart of the budget entries
#This is for Sprint 3
def generate_report(main_screen):
    connection = sqlite3.connect("budget.db")
    cursor = connection.cursor()
    cursor.execute("SELECT category, SUM(CAST(amount AS REAL)) FROM budget_entries GROUP BY category")
    rows = cursor.fetchall()

    if rows:
        # Display report in a new window
        report_window = tk.Toplevel(main_screen)
        report_window.title("Budget Report")
        report_window.geometry('540x400')
        report_window.configure(bg='#333333')

        report_text = tk.Text(report_window, wrap=tk.WORD, font=("Arial", 14))
        report_text.pack(expand=True, fill=tk.BOTH)

        total_amount = 0
        categories = []
        amounts = []

        for row in rows:
            category, total = row
            categories.append(category)
            amounts.append(total)
            report_text.insert(tk.END, f"Category: {category}, Total Amount: ${total:.2f}\n")
            total_amount += total

        report_text.insert(tk.END, f"\nTotal Budget: ${total_amount:.2f}")

        # Generate Pie Chart
        generate_pie_chart(categories, amounts)

        connection.close()
    else:
        messagebox.showinfo("No Entries", "No budget entries found.")

# Function to generate a pie chart of budget categories
def generate_pie_chart(categories, amounts):
    fig, ax = plt.subplots()
    ax.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    ax.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.

    # Save the chart as an image
    fig.savefig('budget_pie_chart.png')

    # Show the pie chart in a new window
    pie_chart_window = tk.Toplevel()
    pie_chart_window.title("Pie Chart")
    pie_chart_window.geometry('540x400')

    img = Image.open('budget_pie_chart.png')
    img = img.resize((400, 400))
    bg_image = ImageTk.PhotoImage(img)
    background_label = tk.Label(pie_chart_window, image=bg_image)
    background_label.image = bg_image  # Keep a reference to prevent garbage collection
    background_label.pack()



# Function to display the main screen
def show_main_screen(root):
    # Create the main screen window
    main_screen = tk.Toplevel(root)
    main_screen.title("Budget App - Main Screen")
    main_screen.geometry('540x600')
    main_screen.configure(bg='#333333')

    frame = tk.Frame(main_screen, bg="#333333")

    # Load logo image for the main screen
    #img = Image.open("logo.png")
    #img = img.resize((400, 200))
    #photo = ImageTk.PhotoImage(img)
    #background_label = tk.Label(frame, image=photo, bg="#333333")
    #background_label.image = photo  # Keep a reference to prevent garbage collection


    # Create buttons with their respective functions
    add_button = tk.Button(frame, text="Add Entry", bg="lightblue", font=("Arial", 16), command=lambda: add_budget(main_screen))
    update_button = tk.Button(frame, text="Update Entry", bg="lightgreen", font=("Arial", 16), command=lambda: update_budget(main_screen))
    delete_button = tk.Button(frame, text="Delete Entry", bg="lightcoral", font=("Arial", 16), command=lambda: delete_budget(main_screen))
    display_button = tk.Button(frame, text="Display All Entries", bg="lightyellow", font=("Arial", 16), command=lambda: display_all_entries(main_screen))
    report_button = tk.Button(frame, text="Generate Report", bg="lightgray", font=("Arial", 16), command=lambda: generate_report(main_screen))


    # Widget placements
    #background_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=10)
    add_button.grid(row=1, column=0, columnspan=2, pady=10)
    update_button.grid(row=2, column=0, columnspan=2, pady=10)
    delete_button.grid(row=3, column=0, columnspan=2, pady=10)
    display_button.grid(row=4, column=0, columnspan=2, pady=10)
    report_button.grid(row=5, column=0, columnspan=2, pady=10) #here is sprint3's report button

    frame.pack()

    main_screen.protocol("WM_DELETE_WINDOW", lambda: close_main_screen(main_screen))

    # Function to close the main screen and return to login screen
    def close_main_screen(screen):
        screen.destroy()
        root.deiconify()  # Show the login screen again
        
    main_screen.protocol("WM_DELETE_WINDOW", lambda: close_main_screen(main_screen))

# Start the application with login screen
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide login screen initially
    from login import login  # Importing login function after Tk root is created
    login(root)
