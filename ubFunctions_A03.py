### UB Umgang mit Functions in Python
#
### Aufgabe 3:
#
### Entwerfen Sie eine Function anrede, die als Parameter einen Vornamen 
### und einen Nachnamen übernimmt und diese  in die Ausgabe „Guten Morgen + ….“mit einbaut.
### Beispiel:
###    • Übergabewert „Thomas“, "Maier"
###    • Ausgabe: „Guten Morgen Thomas Maier“

# In diesem Fall empfängt die Function anrede beim Aufruf die Informationen "Thomas"
# und "Maier".
# Diese Informationen werden in der lokalen Speicherstellen vorname und nachname abgelegt
# und in der Function weiter verarbeitet.

def anrede(vorname, nachname):
    print("Guten Morgen" + " " + vorname + " " + nachname)

    # Beachte, dass diese Function keinen Return-Wert besitzt, da sie die
    # Information lediglich ausgibt

# Aufruf im Hauptprogramm

# Die Function liefert keinen Rückgabewert. Die Funktionalität, die von der
# Aufgabenstellung verlangt wird, liefert die function anrede() selbst.  

# Die beiden Informationen "Thomas" und "Maier" werden an die Function anrede(...)
# zur Verarbeitung übergeben.

anrede("Thomas","Maier") 