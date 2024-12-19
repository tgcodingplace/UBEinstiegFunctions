### UB Umgang mit Functions in Python
#
### Aufgabe 4:
#
### Entwerfen Sie eine Function anrede, die als Parameter einen Vornamen, einen Nachnamen 
### und das Geschlecht übernimmt. Im Falle einer männlichen Person wäre der Parameter 1, 
### im Falle einer weiblichen Person hätte der Übergabeparameter den Wert 0. 
### Die Anrede soll wie in den vorangegangenen Aufgaben aufgebaut sein. 
#
### Beispiel:
###    • Übergabewert „Thomas“, „Maier“, 1	
###    • Ausgabe: „Guten Morgen Herr Thomas Maier“
###	oder
###    • Übergabewert „Sabine“, „Schmidt“, 0	
###    • Ausgabe: „Guten Morgen Frau Sabine Schmidt“

# In diesem Fall empfängt die Function anrede beim Aufruf die Informationen "Sabine",
# "Schmidt" und eine Zahl, die für das Geschlecht steht.
# Diese Informationen werden in der lokalen Speicherstellen vorname, nachname und g abgelegt
# und in der Function weiter verarbeitet.

def anrede(vorname, nachname, g):

    # Wir belegen die lokale Variable temp mit der Information "Herr" vor.
    # "Könnte ja sein, dass es stimmt"
    temp = "Herr"

    # Jetzt überprüfen wir, ob es stimmt. Sollte das übergebene Geschlecht nun weiblich sein
    # ändern wir den Inhalt von temp auf "Frau"
    if g==0:
        temp = "Frau"

    # Im letzten Schritt basteln wir die verlangte Ausgabe zusammen
    print("Guten Morgen" + " " + temp + " " + vorname + " " + nachname)

    # Beachte, dass diese Function keinen Return-Wert besitzt, da sie die
    # Information lediglich ausgibt

# Aufruf im Hauptprogramm

# Die Function liefert keinen Rückgabewert. Die Funktionalität, die von der
# Aufgabenstellung verlangt wird, liefert die function anrede() selbst.  

# Die beiden Informationen "Sabine", "Schmidt" und die Zahl 1 für das Geschlecht
# werden an die Function anrede(...) zur Verarbeitung übergeben.

anrede("Sabine","Schmidt",0) 