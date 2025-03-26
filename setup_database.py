import sqlite3

# Create users database and table
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

# Create the 'users' table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")
connection.commit()
connection.close()

# Create budget database and table
connection = sqlite3.connect("budget.db")
cursor = connection.cursor()

# Create the 'budget_entries' table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS budget_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    amount REAL,
    date DATE
)
""")
connection.commit()
connection.close()

print("Databases and tables have been set up successfully.")