from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import random
from datetime import datetime
import plotly.graph_objects as go
import daten
import berechnung


app = Flask("templates")

@app.route("/")
def start():
    gipfelbuch = daten.gipfel_laden()
    summedauer = berechnung.summedauer()
    summedistanz = berechnung.summedistanz()
    summehoehenmeter = berechnung.summehoehenmeter()
    for key, value in gipfelbuch.items():
        titel = value.keys()
        inhalt = gipfelbuch.items()
        return render_template("auswertung.html", titel=titel, inhalt=inhalt, summedauer=summedauer, summedistanz=summedistanz, summehoehenmeter=summehoehenmeter)


@app.route("/auswertung", methods=["GET", "POST"])
def auswertung():
    if request.method == "POST":
        inhalt2 = berechnung.anzeigeauswertung()
    gipfelbuch = daten.gipfel_laden()
    for key, value in gipfelbuch.items():
        titel = value.keys()
        inhalt = gipfelbuch.items()
        print(inhalt)
        return render_template("auswertung.html", titel=titel, inhalt=inhalt, inhalt2=inhalt2)

@app.route("/eingabe", methods=["GET", "POST"])
def eingabe():
    if request.method == "POST":
        id = datetime.now()
        gipfel = request.form.get('gipfelname')
        koordinatelaenge = request.form.get('koordinatelaenge')
        koordinatebreite = request.form.get('koordinatebreite')
        kanton = request.form.get('kanton')
        datum = request.form.get('datum')
        dauer = request.form.get('dauer')
        distanz = request.form.get('distanz')
        hoehenmeter = request.form.get('hoehenmeter')
        sportart = request.form.get('sportart')
        daten.speichern("gipfel.json", id, {"Gipfel" : gipfel, "KoordinateLaenge" : koordinatelaenge, "KoordinateBreite" : koordinatebreite, "Kanton" : kanton, "Datum" : datum, "Dauer" : dauer, "Distanz" : distanz, "Hoehenmeter" : hoehenmeter, "Sportart" : sportart})
        return f"Zum Zeitpunkt {id} wurde der Peak {gipfel} hinzugefügt."

    return render_template("eingabe.html")

@app.route("/bearbeitung")
def bearbeitung():
    fig = berechnung.anzahlkanton()
    return render_template("bearbeitung.html", fig=fig)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

