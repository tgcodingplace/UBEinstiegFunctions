### UB Umgang mit Functions in Python
#
### Aufgabe 3 - jetzt mit Rückgabewert.
#
### Entwerfen Sie eine Function anrede, die als Parameter einen Vornamen 
### und einen Nachnamen übernimmt und diese in „Guten Morgen + ….“ mit einbaut.
### Die zusammengesetzte Information soll am Ende der Function an den Aufrufer
### zurückkopiert werden.
### Beispiel:
###    • Übergabewert: „Thomas“, "Maier"
###    • Rückgabewert: „Guten Morgen Thomas Maier“

# In diesem Fall empfängt die Function anrede beim Aufruf die Informationen "Thomas"
# und "Maier". Diese Informationen werden in der lokalen Speicherstellen vorname 
# und nachname abgelegt und in der Function weiter verarbeitet.

def anrede(vorname, nachname):
    meldung = "Guten Morgen" + " " + vorname + " " + nachname

    # Die zusammengesetzte Information wird an den Aufrufer zurückkopiert.
    return meldung

# Aufruf im Hauptprogramm

# Die Funktionalität, die von der Aufgabenstellung verlangt wird, 
# liefert die function anrede() selbst.  

# Die beiden Informationen "Thomas" und "Maier" werden an die Function anrede(...)
# zur Verarbeitung übergeben.
#
# Der Rückgabewert der Function wird im Hauptprogramm ausgegeben.

print(anrede("Thomas","Maier")) 