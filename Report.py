import sqlite3

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

# Total Income
cursor.execute(
    "SELECT SUM(amount) FROM transactions WHERE type='Income'"
)
income = cursor.fetchone()[0] or 0

# Total Expense
cursor.execute(
    "SELECT SUM(amount) FROM transactions WHERE type='Expense'"
)
expense = cursor.fetchone()[0] or 0

# Balance
balance = income - expense

print("Total Income:", income)
print("Total Expense:", expense)
print("Balance:", balance)

conn.close()