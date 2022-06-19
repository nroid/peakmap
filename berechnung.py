import plotly.graph_objects as go
from flask import render_template
from flask import request
import json
import daten
import main
import plotly.express as px
from plotly.offline import plot

"""
Funktion berechnet aus den Daten von gipfel.json die Anzahl Touren pro Kanton und gibt die Werte für
die Darstellung im Balkendiagramm zurück
"""
def anzahlkanton():
    gipfelbuch = daten.gipfel_laden()
    ag = 0
    ai = 0
    ar = 0
    be = 0
    bl = 0
    bs = 0
    fr = 0
    ge = 0
    gl = 0
    gr = 0
    ju = 0
    lu = 0
    ne = 0
    nw = 0
    ow = 0
    sg = 0
    sh = 0
    so = 0
    sz = 0
    tg = 0
    ti = 0
    ur = 0
    vd = 0
    vs = 0
    zg = 0
    zh = 0

    for key, value in gipfelbuch.items():
        if value["Kanton"] == "AG":
            ag += 1
        elif value["Kanton"] == "AI":
            ai += 1
        elif value["Kanton"] == "AR":
            ar += 1
        elif value["Kanton"] == "BE":
            be += 1
        elif value["Kanton"] == "BL":
            bl += 1
        elif value["Kanton"] == "BS":
            bs += 1
        elif value["Kanton"] == "FR":
            fr += 1
        elif value["Kanton"] == "GE":
            ge += 1
        elif value["Kanton"] == "GL":
            gl += 1
        elif value["Kanton"] == "GR":
            gr += 1
        elif value["Kanton"] == "JU":
            ju += 1
        elif value["Kanton"] == "LU":
            lu += 1
        elif value["Kanton"] == "NE":
            ne += 1
        elif value["Kanton"] == "NW":
            nw += 1
        elif value["Kanton"] == "OW":
            ow += 1
        elif value["Kanton"] == "SG":
            sg += 1
        elif value["Kanton"] == "SH":
            sh += 1
        elif value["Kanton"] == "SO":
            so += 1
        elif value["Kanton"] == "SZ":
            sz += 1
        elif value["Kanton"] == "TG":
            tg += 1
        elif value["Kanton"] == "TI":
            ti += 1
        elif value["Kanton"] == "UR":
            ur += 1
        elif value["Kanton"] == "VD":
            vd += 1
        elif value["Kanton"] == "VS":
            vs += 1
        elif value["Kanton"] == "ZG":
            zg += 1
        elif value["Kanton"] == "ZH":
            zh += 1

    kantone = ['AG', 'AI', 'AR', 'BE', 'BL', 'BS', 'FR', 'GE', 'GL', 'GR', 'JU', 'LU', 'NE', 'NW', 'OW', 'SG', 'SH', 'SO', 'SZ', 'TG', 'TI', 'UR', 'VD', 'VS', 'ZG', 'ZH']
    values = [ag, ai, ar, be, bl, bs, fr, ge, gl, gr, ju, lu, ne, nw, ow, sg, sh, so, sz, tg, ti, ur, vd, vs, zg, zh]

    return kantone, values

# Berechnung der Summe der Dauer aller gipfel.json Einträge
def summedauer():
    gipfelbuch = daten.gipfel_laden()
    summedauer = 0.0
    for key, value in gipfelbuch.items():
        summedauer += float(value["Dauer"])
    return summedauer

# Berechnung der Summe der Distanzen aller gipfel.json Einträge
def summedistanz():
    gipfelbuch = daten.gipfel_laden()
    summedistanz = 0
    for key, value in gipfelbuch.items():
        summedistanz += int(value["Distanz"])
    return summedistanz

# Berechnung der Summe der Höhenmeter aller gipfel.json Einträge
def summehoehenmeter():
    gipfelbuch = daten.gipfel_laden()
    summehoehenmeter = 0
    for key, value in gipfelbuch.items():
        summehoehenmeter += int(value["Hoehenmeter"])
    return summehoehenmeter

# Erstellung des Balkendiagramms der Anzahl Routen pro Kanton
def viz():
    kantone, values = anzahlkanton()
    fig = px.bar(x=kantone, y=values)
    div = plot(fig, output_type="div")
    return div
