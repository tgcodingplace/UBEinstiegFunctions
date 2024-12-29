### UB Umgang mit Functions in Python
#
### Aufgabe 9:
#
### Entwerfen Sie eine Function f4, die überprüft, ob von zwei übergebenen ganzzahligen
### Werten die zweite Zahl ein ganzzahliger Teiler der ersten Zahl ist


def f4(a, b):

    meldung = " ist kein ganzzahliger Teiler von "

    if a%b==0:
        meldung = " ist ein ganzzahliger Teiler von "  

    return str(b) + meldung + str(a)

# Aufruf im Hauptprogramm

x = int(input("Eingabe Zahl 1: "))
y = int(input("Eingabe Zahl 2: "))

print(f4(x,y))
