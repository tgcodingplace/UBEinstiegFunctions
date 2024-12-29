### UB Umgang mit Functions in Python
#
### Aufgabe 7:
#
### Entwerfen Sie eine Function f2, die von einem übergebenen ganzzahligen Wert die
### Quadratzahl zurückliefert.


def f2(wert):

    return wert*wert
    # alternativ: wert**2

# Aufruf im Hauptprogramm

eingabe = int(input("Eingabe einer Ganzzahl: "))

print("Die Quadratzahl von " + str(eingabe) + " lautet " + str(f2(eingabe)))