import sqlite3

connection = sqlite3.connect("notes.db")

connection.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL
    )
""")

connection.commit()

connection.execute(
    "INSERT INTO notes (content) VALUES (?)",
    ("My first Flask note",)
)

rows = connection.execute("SELECT * FROM notes").fetchall()

print(rows)

connection.commit()
connection.close()