from flask import Flask, render_template, request
import sqlite3

app=Flask(__name__)

notes=[]


@app.route("/", methods=["GET", "POST"])
def home():

    connection = sqlite3.connect("my_notes.db")

    connection.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL
    )
    
    """)
    connection.commit()

    if request.method == "POST":
        note=request.form["note"]

        connection.execute(
            "INSERT INTO notes (content) VALUES (?)",
            (note,)
        )
        connection.commit()
        rows = connection.execute("SELECT * FROM notes").fetchall()

        connection.close()

    return render_template("index.html",notes=rows)
    
if __name__=="__main__":
    app.run(debug=True)