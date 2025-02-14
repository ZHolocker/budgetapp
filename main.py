import login  # Import the login page from the other file
from flask import Flask, request, render_template
import pandas as pd

class expense:
    """creates the expense class, so it had details for each transaction"""
    def __init__(self, amount, date, description):
        self.amount = amount
        self.date = date
        self.description = description
    
#create the list to hold the expenses   
expenses = []
    
def add_expense(expense, expenses):
    """this adds expenses to the list"""
    for expense in expenses:
        if expense not in expenses:
            expenses.append(expense)
        else:
            print("Expense already listed")
        


def remove_expense(expense, expenses):
    """This removes an expense from the list"""
    for expense in expenses:
        if expense in expenses:
            expenses.remove(expense)
        else:
            print("Invalid expense")


def show_expenses(expenses):
    """this shows the expenses in the list"""
    for e in expenses:
        print(e)











if __name__ == "__main__":
    root.mainloop()  # Run the login page
