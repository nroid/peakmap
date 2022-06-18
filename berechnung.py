import plotly.graph_objects as go
from flask import render_template
from flask import request
import json
import daten
import main

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
    kantonsumme = 0

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

    kantonsumme += ag
    kantonsumme += ai
    kantonsumme += ar
    kantonsumme += be
    kantonsumme += bl
    kantonsumme += bs
    kantonsumme += fr
    kantonsumme += ge
    kantonsumme += gl
    kantonsumme += gr
    kantonsumme += ju
    kantonsumme += lu
    kantonsumme += ne
    kantonsumme += nw
    kantonsumme += ow
    kantonsumme += sg
    kantonsumme += sh
    kantonsumme += so
    kantonsumme += sz
    kantonsumme += tg
    kantonsumme += ti
    kantonsumme += ur
    kantonsumme += vd
    kantonsumme += vs
    kantonsumme += zg
    kantonsumme += zh

    kantone = ['AG', 'AI', 'AR', 'BE', 'BL', 'BS', 'FR', 'GE', 'GL', 'GR', 'JU', 'LU', 'NE', 'NW', 'OW', 'SG', 'SH', 'SO', 'SZ', 'TG', 'TI', 'UR', 'VD', 'VS', 'ZG', 'ZH']
    values = [ag, ai, ar, be, bl, bs, fr, ge, gl, gr, ju, lu, ne, nw, ow, sg, sh, so, sz, tg, ti, ur, vd, bs, zg, zh]

    fig = go.Figure(data=[go.Pie(labels=kantone, values=values, insidetextorientation='radial')])
    return fig
    #fig.show()

def summedauer():
    gipfelbuch = daten.gipfel_laden()
    summedauer = 0.0
    for key, value in gipfelbuch.items():
        summedauer += float(value["Dauer"])
    return summedauer

def summedistanz():
    gipfelbuch = daten.gipfel_laden()
    summedistanz = 0
    for key, value in gipfelbuch.items():
        summedistanz += int(value["Distanz"])
    return summedistanz

def summehoehenmeter():
    gipfelbuch = daten.gipfel_laden()
    summehoehenmeter = 0
    for key, value in gipfelbuch.items():
        summehoehenmeter += int(value["Hoehenmeter"])
    return summehoehenmeter

def anzeigeauswertung():
    kantonsauswahl = request.form.get('kanton')
    gipfelbuch = daten.gipfel_laden()
    inhalt2 = "test"
    kubli = "test"
    if kantonsauswahl == "AG":
        for key, value in gipfelbuch.items():
            if value["Kanton"] == "AG":
                inhalt2 = value
                print(value)
            #     nemro = value.keys()
            #     kubli = gipfelbuch.items()
                return inhalt2

    # elif kantonsauswahl == "AI":
    #
    # elif kantonsauswahl == "AR":
    # elif kantonsauswahl == "BE":
    # elif kantonsauswahl == "BL":
    # elif kantonsauswahl == "BS":
    # elif kantonsauswahl == "AI":
    # elif kantonsauswahl == "FR":
    # elif kantonsauswahl == "GE":
    # elif kantonsauswahl == "GL":
    # elif kantonsauswahl == "GR":
    # elif kantonsauswahl == "JU":
    # elif kantonsauswahl == "LU":
    # elif kantonsauswahl == "NE":
    # elif kantonsauswahl == "NW":
    # elif kantonsauswahl == "OW":
    # elif kantonsauswahl == "SG":
    # elif kantonsauswahl == "SH":
    #
    # elif kantonsauswahl == "SO":
    #
    # elif kantonsauswahl == "SZ":
    #
    # elif kantonsauswahl == "TG":
    #
    # elif kantonsauswahl == "TI":
    #
    # elif kantonsauswahl == "UR":
    #
    # elif kantonsauswahl == "VD":
    #
    # elif kantonsauswahl == "VS":
    #
    # elif kantonsauswahl == "ZG":
    #
    # elif kantonsauswahl == "ZH":
    #
    # else


