### UB Umgang mit Functions in Python
#
### Aufgabe 18:
#
### Entwerfen Sie eine Function f12, die überprüft, ob ein übergebenes Wort ein Palindrom
### ist. Geben Sie das Ergebnis der Prüfung in Form eines boolschen Wertes an den Aufrufer
### zurück.

### Ein Palindrom ist ein Wort, dass sowohl vorwärts als auch rückwärts gelesen identisch ist.

def f12(wort):

    turn = ""

    # i ist der aktuelle buchstabe des Wortes, das in wort gespeichert ist
    # in turn werden die Buchstaben in umgekehrter Reihenfolge abgelegt.
    for i in wort:
        turn = i + turn

    return wort==turn

# Aufruf im Hauptprogramm

eingabe = input("Gib mir ein Wort: ")

meldung = "Palindrom"

if not f12(eingabe):
    meldung = "kein " + meldung

print(meldung)
