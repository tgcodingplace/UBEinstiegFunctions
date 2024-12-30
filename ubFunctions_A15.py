### UB Umgang mit Functions in Python
#
### Aufgabe 15:
#
### Entwerfen Sie eine Function f9, die eine positive Dezimalzahl im 8-Bit-Bereich in der
### dualen Darstellung zurückliefert. Der Typ den Rückgabewertes soll ein String sein.

def f9(wert):

    # Im 8-Bit-Bereich (0-255) ist 128 der größte Teiler
    teiler = 128

    # In die Speicherstelle bitfolge legen wir die duale Darstellung ab
    bitfolge = ""

    # Wiederhole solange teiler größer als 0 ist. Durch die fortlaufende ganzzahlige
    # Division durch 2 stellen wir sicher, dass alle 8 Bit (=Stellen) geprüft werden
    # Ist der Teiler im aktuellen Wert vorhanden, schreiben wir eine 1, ansonsten eine
    # 0. Nach jeder Division rechnen wir mit dem Divisionsrest weiter.

    while teiler > 0:

        bitfolge = bitfolge + str(wert//teiler)

        wert = wert % teiler

        teiler = teiler // 2

    # Ok, wir schicken die bitfolge an den Aufrufer zurück
    return bitfolge


# Aufruf im Hauptprogramm

eingabe = int(input("Gib mir eine Dezimalzahl [0..255]: "))

# Aufruf und Ausgabe des Rückgabewertes
print("Die duale Darstellung der Dezimalzahl " + str(eingabe), end=" ")
print("lautet " + f9(eingabe))
