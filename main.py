from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import random
from datetime import datetime
import daten


app = Flask("templates")


@app.route("/")
def start():
    return render_template("auswertung.html")

@app.route("/auswertung")
def auswertung():
    return render_template("auswertung.html")

@app.route("/eingabe/", methods=["GET", "POST"])
def eingabe():
    if request.method == "POST":
        id = datetime.now()
        gipfel = request.form.get('gipfelname')
        koordinatelaenge = request.form.get('koordinatelaenge')
        koordinatebreite = request.form.get('koordinatebreite')
        kanton = request.form.get('kanton')
        daten.speichern("gipfel.json", id, {"Gipfel" : gipfel, "KoordinateLaenge" : koordinatelaenge, "KoordinateBreite" : koordinatebreite, "Kanton" : kanton})
        return f"Zum Zeitpunkt {id} wurde der Peak {gipfel} hinzugefügt."

    return render_template("eingabe.html")

@app.route("/bearbeitung")
def bearbeitung():
    return render_template("bearbeitung.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

