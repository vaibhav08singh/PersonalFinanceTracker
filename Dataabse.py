import sqlite3

conn = sqlite3.connect("finance.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
id INTEGER PRIMARY KEY AUTOINCREMENT,
amount REAL,
category TEXT,
type TEXT,
date TEXT
)
""")

conn.commit()
conn.close()

print("Database Created")