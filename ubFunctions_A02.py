### UB Umgang mit Functions in Python
#
### Aufgabe 2:
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
    print("Guten Morgen" + " " + vorname)

    # Beachte, dass diese Function keinen Return-Wert besitzt, da sie die
    # Information lediglich ausgibt

# Aufruf im Hauptprogramm

# Die Function liefert keinen Rückgabewert. Die Funktionalität, die von der
# Aufgabenstellung verlangt wird, liefert die function anrede() selbst.  
anrede("Thomas") 