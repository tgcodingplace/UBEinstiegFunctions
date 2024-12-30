### UB Umgang mit Functions in Python
#
### Aufgabe 16:
#
### Entwerfen Sie eine Function f10, die eine positive Dezimalzahl im 8-Bit-Bereich in der
### hexadezimalen Darstellung zurückliefert. Der Typ den Rückgabewertes soll ein String
### sein.

def f10(wert):

    # Im 8-Bit-Bereich (0-255) ist 16 der größte Teiler
    teiler = 16
    # In die Speicherstelle bitfolge legen wir die duale Darstellung ab
    hexfolge = ""

    # Wiederhole solange teiler größer als 0 ist. Durch die fortlaufende ganzzahlige
    # Division durch 2 stellen wir sicher, dass alle 8 Bit (=Stellen) geprüft werden
    # Ist der Teiler im aktuellen Wert vorhanden, schreiben wir den entsprechenden 
    # Faktor, ansonsten eine 0. 
    # Nach jeder Division rechnen wir mit dem Divisionsrest weiter.

    while teiler > 0:

        hexziffer = ""

        # An dieser Stelle arbeiten wir mit dem ASCII-Code 55 + 10 = 65 --> "A"
        # chr() macht aus einer Zahl das entsprechende Zeichen

        if wert//teiler > 9:
            hexziffer = chr(55+wert//teiler)
        else:
            hexziffer = str(wert//teiler)

        hexfolge = hexfolge + hexziffer

        wert = wert % teiler

        teiler = teiler // 16

    # Ok, wir schicken die bitfolge an den Aufrufer zurück
    return hexfolge


# Aufruf im Hauptprogramm

eingabe = int(input("Gib mir eine Dezimalzahl [0..255]: "))

# Aufruf und Ausgabe des Rückgabewertes
print("Die hexadezimale Darstellung der Dezimalzahl " + str(eingabe), end=" ")
print("lautet " + f10(eingabe))
