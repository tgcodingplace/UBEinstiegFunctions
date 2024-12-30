### UB Umgang mit Functions in Python
#
### Aufgabe 13: ( im Prinzip Aufgabe 12 mit Rückgabewert )
#
### Entwerfen Sie eine Function f7, die alle geraden Zahlen in einem übergebenen Intervall
### zurück gibt. Die Intervallgrenzen sind nicht Bestandteil der Ausgabe.

def f7(a, b):

    # In diese lokale Variable schreiben wir die Zahlenreihe
    meldung = ""

    # Wenn die Intervallgrenze eine gerade Zahl ist erhöhe um 2, denn die Intervallgrenze
    # darf nicht Bestandteil der Ausgabe sein. Erhöhe um 2 auf die nächste gerade Zahl
    # Wäre der Startwert ungerade so erhöhe um 1 auf die nächte gerade Zahl

    if a%2==0:
        a+=2
    else:
        a+=1

    # Startwert ist a, Grenze ist b, erhöhe um 2
    # Schreibe die Zahlenreihe in die Variable reihe
    for i in range(a,b,2):
        meldung = meldung + str(i) + " "

    # Ok, wir schicken die in meldung abgelegte Zeichenkette an den Aufrufer
    # zurück
    return meldung


# Aufruf im Hauptprogramm

start = int(input("Startwert: "))
ende  = int(input("Endwert  : "))

# Aufruf und Ausgabe des Rückgabewertes
print(f7(start, ende))
