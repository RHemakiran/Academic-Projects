import os
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime

# File to store expenses
EXPENSE_FILE = "expenses.txt"

# Load expenses from file
def load_expenses():
    if not os.path.exists(EXPENSE_FILE):
        return []
    
    expenses = []
    with open(EXPENSE_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:  # Ensure the line has Date, Category, and Amount
                expenses.append(parts)
    
    return expenses


# Save expenses to file
def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as file:
        for expense in expenses:
            file.write(",".join(expense) + "\n")

# Update listbox and total
def update_listbox():
    expense_listbox.delete(0, tk.END)
    total = 0
    for date, category, amount in expenses:
        expense_listbox.insert(tk.END, f"{date} | {category}: ${amount}")
        total += float(amount)
    total_label.config(text=f"Total Expenses: ${total:.2f}")

# Add a new expense
def add_expense():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()

    if category and amount:
        try:
            float(amount)  # Check if amount is a valid number
            expenses.append((date, category, amount))
            save_expenses(expenses)
            update_listbox()
            category_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Amount must be a number!")
    else:
        messagebox.showwarning("Input Error", "Please enter category and amount.")

# Delete selected expense
def delete_expense():
    try:
        selected_index = expense_listbox.curselection()[0]
        expenses.pop(selected_index)
        save_expenses(expenses)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select an expense to delete.")

# Initialize main GUI window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("450x500")
root.configure(bg="#f0f0f0")

# Load existing expenses
expenses = load_expenses()

# UI Components
tk.Label(root, text="Date:", font=("Arial", 12), bg="#f0f0f0").pack()
date_entry = DateEntry(root, width=15, font=("Arial", 12))
date_entry.pack()

tk.Label(root, text="Category:", font=("Arial", 12), bg="#f0f0f0").pack()
category_entry = tk.Entry(root, font=("Arial", 12))
category_entry.pack()

tk.Label(root, text="Amount:", font=("Arial", 12), bg="#f0f0f0").pack()
amount_entry = tk.Entry(root, font=("Arial", 12))
amount_entry.pack()

add_button = tk.Button(root, text="Add Expense", font=("Arial", 12), bg="#4CAF50", fg="white", command=add_expense)
add_button.pack(pady=5)

expense_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
expense_listbox.pack()

delete_button = tk.Button(root, text="Delete Selected", font=("Arial", 12), bg="#f44336", fg="white", command=delete_expense)
delete_button.pack(pady=5)

# Total Expenses Label
total_label = tk.Label(root, text="Total Expenses: $0.00", font=("Arial", 14, "bold"), bg="#f0f0f0")
total_label.pack(pady=10)

update_listbox()  # Show existing expenses
root.mainloop()

#cd H:\PYTHON
