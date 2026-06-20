import sqlite3

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

cursor.execute("""
UPDATE transactions
SET type='Expense'
WHERE id=1
""")

conn.commit()
conn.close()

print("Updated Successfully")