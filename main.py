from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import random
from datetime import datetime
import daten


app = Flask("Daten")


@app.route("/")
def start():
    return render_template("auswertung.html")

@app.route("/auswertung")
def auswertung():
    return render_template("auswertung.html")

@app.route("/eingabe", methods=["get", "post"])
def eingabe():
    if request.method.lower() == "get":
        return render_template('eingabe.html')
    if request.method.lower() == "post":
        gipfel = request.form['gipfelname']
        return gipfel

@app.route("/bearbeitung")
def bearbeitung():
    return render_template("bearbeitung.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

