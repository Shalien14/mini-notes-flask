from flask import Flask, render_template, request, redirect
import sqlite3

app=Flask(__name__)



connection = sqlite3.connect("my_notes.db")
connection.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL
)

""")
connection.commit()
connection.close()

@app.route("/", methods=["GET", "POST"])
def home():

    connection = sqlite3.connect("my_notes.db")

    if request.method == "POST":
        note=request.form["note"]

        connection.execute(
            "INSERT INTO notes (content) VALUES (?)",
            (note,)
        )
        connection.commit()
        return redirect("/")
    rows = connection.execute("SELECT * FROM notes").fetchall()
    connection.close()

    return render_template("index.html",notes=rows)

@app.route("/delete", methods=["POST"])
def delete():
    note_id=request.form["id"]

    connection = sqlite3.connect("my_notes.db")
    connection.execute(
        "DELETE FROM notes WHERE id= ?",
        (note_id,)
    )
    connection.commit()
    connection.close()

    return redirect("/")

@app.route("/edit", methods=["GET","POST"])
def edit():
    connection = sqlite3.connect("my_notes.db")

    if request.method == "POST":
        note_id = request.form["id"]
        new_note = request.form["note"]
        connection.execute(
            "UPDATE notes SET content = ? WHERE id = ?",
            (new_note, note_id)
        )
        connection.commit()
        connection.close()
        return redirect("/")
    
    note_id=request.args["id"]
    note = connection.execute(
        "SELECT * FROM notes WHERE id = ?",
        (note_id,)
    ).fetchone()
    connection.close()
    
    return render_template("edit.html", note=note)
    

if __name__=="__main__":
    app.run(debug=True)