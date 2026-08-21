from flask import Flask, render_template, request

app=Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():

    note=""

    if request.method == "POST":
        note=request.form["note"]
        print(note)
    return render_template("index.html",note=note)

if __name__=="__main__":
    app.run(debug=True)