### UB Umgang mit Functions in Python
#
### Aufgabe 2: - jetzt in der Variante mit Rückgabewert
#
### Entwerfen Sie eine Function anrede, die als Parameter einen Vornamen übernimmt und 
### diesen in die Ausgabe „Guten Morgen + ….“mit einbaut.
### Beispiel:
###    • Übergabewert „Thomas“
###    • Ausgabe: „Guten Morgen Thomas“

# In diesem Fall empfängt die Function anrede beim Aufruf die Information "Thomas".
# Diese Information wird in der lokalen Speicherstelle vorname abgelegt und in der
# Function weiter verarbeitet.

def anrede(vorname):
    
    return "Guten Morgen" + " " + vorname

    # Beachte, dass diese Function eine Zeichenkette aus drei Teilen zusammenstellt.
    # Teil 1: "Guten Morgen"
    # Teil 2: " " --> Leerzeichen
    # Teil 3: übergebener Vorname
    #
    # Die aus diesen drei Teilen kontruierte Zeichenkette wird mit Hilfe des 
    # return-Befehls an den Aufrufer zurückkopiert.

# Aufruf im Hauptprogramm

# Die Function liefert einen Rückgabewert. Dieser muss ausgegeben werden.

print(anrede("Thomas")) 