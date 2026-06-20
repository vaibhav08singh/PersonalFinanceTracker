import sqlite3

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

amount = float(input("Enter Amount: "))
category = input("Enter Category: ")
type = input("Enter Type (Income/Expense): ")
date = input("Enter Date (YYYY-MM-DD): ")

cursor.execute(
    "INSERT INTO transactions(amount, category, type, date) VALUES (?, ?, ?, ?)",
    (amount, category, type, date)
)

conn.commit()
conn.close()

print("Transaction Added Successfully")