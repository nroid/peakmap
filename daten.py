from datetime import datetime
import json

# Speichert die mitgelieferten Daten in der mitgelieferten Datei ab
def speichern(datei, key, value):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)

# Lädt Dateiinhalt und gibt Inhalt zurück
def gipfel_laden():
    datei_name = "gipfel.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt
