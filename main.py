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

"""
Daten werden aus gipfel.json geladen
Summe der Dauer wird berechnet
Summe der Distanz wird berechnet
Summe der Höhenmeter wird berechnet
Balkendiagramm wird erstellt
Titel wird aus Daten extrahiert
Inhalt Gipfelbuch wird extrahiert
Variablen werden an auswertung.html übergeben
"""
@app.route("/", methods=["GET", "POST"])
def start():
    gipfelbuch = daten.gipfel_laden()
    summedauer = berechnung.summedauer()
    summedistanz = berechnung.summedistanz()
    summehoehenmeter = berechnung.summehoehenmeter()
    div = berechnung.viz()
    sport = berechnung.sport()
    for key, value in gipfelbuch.items():
        titel = value.keys()
        inhalt = gipfelbuch.items()
        return render_template("auswertung.html", titel=titel, inhalt=inhalt, summedauer=summedauer, summedistanz=summedistanz, summehoehenmeter=summehoehenmeter, viz_div=div, sport=sport)

"""
Daten werden aus gipfel.json geladen
Summe der Dauer wird berechnet
Summe der Distanz wird berechnet
Summe der Höhenmeter wird berechnet
Balkendiagramm wird erstellt
Titel wird aus Daten extrahiert
Inhalt Gipfelbuch wird extrahiert
Variablen werden an auswertung.html übergeben
"""
@app.route("/auswertung", methods=["GET", "POST"])
def auswertung():
    gipfelbuch = daten.gipfel_laden()
    summedauer = berechnung.summedauer()
    summedistanz = berechnung.summedistanz()
    summehoehenmeter = berechnung.summehoehenmeter()
    div = berechnung.viz()
    sport = berechnung.sport()
    for key, value in gipfelbuch.items():
        titel = value.keys()
        inhalt = gipfelbuch.items()
        return render_template("auswertung.html", titel=titel, inhalt=inhalt, summedauer=summedauer, summedistanz=summedistanz, summehoehenmeter=summehoehenmeter, viz_div=div, sport=sport)

"""
Mit Methods POST, werden Daten aus Eingabeformular in Variablen geschrieben.
Diese werden an Funktion Daten speichern übergeben um in gipfel.json abgespeichert zu werden.
Rückmeldung dass Daten zu Datenbank hinzugefügt wurden.
"""
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
        ausgabe = f"Zum Zeitpunkt {id} wurde der Peak {gipfel} hinzugefügt."
        return render_template("eingabe.html", ausgabe=ausgabe)

    return render_template("eingabe.html")

"""
Bearbeitung ist funktioniert nicht...
Im Dropdown sollte eine Tour ausgewählt werden können. Die Attribute dieser Tour sollten in die Inputboxen abgefüllt werden und somit bearbeitet werden können.
"""
@app.route("/bearbeitung", methods=["GET", "POST"])
def bearbeitung():
    gipfelbuch = daten.gipfel_laden()
    inhalt = gipfelbuch.items()
    return render_template("bearbeitung.html", inhalt=inhalt)

    if request.method == "POST":
        tour = request.form.get('tour')
        return render_template("bearbeitung.html", tour=tour)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

