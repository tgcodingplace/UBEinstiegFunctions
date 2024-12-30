### UB Umgang mit Functions in Python
#
### Aufgabe 17:
#
### Entwerfen Sie eine Function f11, die eine positive Dezimalzahl im 8-Bit-Bereich entweder
### in der dualen oder in der hexadezimalen Darstellung zurückliefert. Die Entscheidung, in
### welchem Zahlensystem der Rückgabewert ist soll ein weiterer Parameter sein. Der Typ
### den Rückgabewertes soll ein String sein.

# modus == 0 --> Dualzahl
# modus == 1 --> hexadezimale Zahl

def f11(wert, modus):

    ausgabe = ""
    teiler = 128
    basis = 2

    if modus == 1:
        teiler = 16
        basis =  16

    while teiler > 0:

        codierung = ""

        # An dieser Stelle arbeiten wir mit dem ASCII-Code 55 + 10 = 65 --> "A"
        # chr() macht aus einer Zahl das entsprechende Zeichen

        if wert//teiler > 9:
            codierung = chr(55+wert//teiler)
        else:
            codierung = str(wert//teiler)

        ausgabe = ausgabe + codierung

        wert = wert % teiler

        teiler = teiler // basis

    # Ok, wir schicken die ausgabe an den Aufrufer zurück
    return ausgabe


# Aufruf im Hauptprogramm

eingabe = int(input("Gib mir eine Dezimalzahl [0..255]: "))
mymode  = int(input("Gib mir das Zahlensystem [0--> Dualzahl; 1 --> Hexadezimalzahl]: "))

zahlensystem = "Dualzahl"

if mymode == 1:
    zahlensystem = "hexadezimale Zahl"

# Aufruf und Ausgabe des Rückgabewertes
print("Die Dezimalzahl " + str(eingabe) + " wird als " + zahlensystem, end=" ")
print("so dargestellt: " + f11(eingabe, mymode))
