import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

cursor.execute("""
SELECT category, SUM(amount)
FROM transactions
WHERE type='Expense'
GROUP BY category
""")

data = cursor.fetchall()

categories = [row[0] for row in data]
amounts = [row[1] for row in data]

plt.figure(figsize=(6,6))
plt.pie(amounts, labels=categories, autopct='%1.1f%%')
plt.title("Expense Distribution")
plt.show()

conn.close()