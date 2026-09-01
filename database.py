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


connection.execute(
    "DELETE FROM notes WHERE id = ?",
    (7,)
)

connection.commit()

rows = connection.execute("SELECT * FROM notes").fetchall()

print(rows)

connection.commit()
connection.close()