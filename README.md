# **PeakMap**

**Problembeschreibung/Motivation**
 - Als begeisterter Outdoorsportler erfasse ich gerne meine Touren, egal ob beim Wandern, Biken oder Skitourengehen. Meine erbrachten Leistungen sehe ich gerne aufgezeichnet und machen mich stolz.
 - Mit PeakMap kann jede Tour mit Informationen wie Distanz, Höhenmeter, Aktivitätsdauer und Sportart erfasst werden. Die erhobenen Daten können einzeln oder in Kategorien zusammengezogen und für einen bestimmten Zeitraum dargestellt werden. So hat der Benutzer seine sportlichen Leistungen jederzeit im Blick.
 - Das Projekt bietet die Möglichkeit Daten zu erfassen, sie zu bearbeiten und in grafischer Form anzuzeigen.

**Betrieb**
 - Für den Betrieb müssen keine zusätzlichen Pakete installiert werden.
 - Für die vollständige Nutzung dieser Webapplikation wird die Aktivierung von JavaScript vorausgesetzt. Dies kann in den Webbrowsereinstellungen aktiviert werden.
 - Zur Verwendung wird die Datei main.py ausgeführt.

**Benutzung**
- Gestartet wird das Projekt auf der Seite der Auswertung. Alle bereits erfassten Daten, welche in der json-Datei abgespeichert sind, werden in einer Tabelle aufgeführt. Nachfolgend wird die Anzahl Touren pro Kanton in einem Balkendiagramm aufgezeigt.
- Auf der Eingabeseite können Daten erfasst werden, welche dann in der json-Datei hinzugefügt werden.

**Architektur**
`![Peak Map](../static/PeakMap_Ablaufdiagramm.png)`

**Ungelöste/unbearbeitete Probleme**
 - Die Bearbeitung der bereits erfassten Daten ist noch nicht umgesetzt.
 - Die einzelnen Touren sollten anhand der gespeicherten Koordinaten auf einer Karte dargestellt werden.
 - Die Touren sollten anhand Dropdown-Menü gefiltert werden können.
