### UB Umgang mit Functions in Python
#
### Aufgabe 11:
#
### Entwerfen Sie eine Function f6, die überprüft, ob ein Prüfling bestanden hat oder nicht.
### Der Prüfling schreibt eine Deutschprüfung, eine Matheprüfung und eine
### Englischprüfung.
### Die Prüfung ist bestanden, wenn der Prüfling im Schnitt nicht schlechtet als 4,0 ist. Die
### Function soll einen boolschen Wert zurückliefern.

def f6(d, m, e):

    schnitt = (d+e+m)/3

    if schnitt <= 4.0:
        return True

    return False

# Aufruf im Hauptprogramm

x = int(input("Note in Deutsch : "))
y = int(input("Note in Mathe   : "))
z = int(input("Note in Englisch: "))

# Wir setzen die Meldung auf bestanden
meldung = "bestanden"

# sollte son der Function ein False zurückkommen schreiben wir ein "nicht " vor die meldung
if not f6(x,y,z):
    meldung = "nicht " + meldung

print("Der Prüfling hat die Prüfung " + meldung)
