import sqlite3

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

cursor.execute("""
SELECT category, SUM(amount)
FROM transactions
WHERE type='Expense'
GROUP BY category
""")

rows = cursor.fetchall()

for category, amount in rows:
    print(f"{category}: ₹{amount}")

conn.close()