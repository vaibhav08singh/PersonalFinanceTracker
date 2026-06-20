import tkinter as tk
import sqlite3
from tkinter import messagebox

def add_transaction():
    amount = amount_entry.get()
    category = category_entry.get()
    trans_type = type_entry.get()
    date = date_entry.get()

    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO transactions(amount, category, type, date) VALUES (?, ?, ?, ?)",
        (amount, category, trans_type, date)
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Transaction Added!")

    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    type_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Personal Finance Tracker")
root.geometry("500x400")

tk.Label(root, text="Personal Finance Tracker", font=("Arial", 18)).pack(pady=10)

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Type (Income/Expense)").pack()
type_entry = tk.Entry(root)
type_entry.pack()

tk.Label(root, text="Date (YYYY-MM-DD)").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Button(
    root,
    text="Add Transaction",
    command=add_transaction
).pack(pady=20)

root.mainloop()