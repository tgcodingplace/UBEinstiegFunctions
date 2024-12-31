### UB Umgang mit Functions in Python
#
### Aufgabe 21:
#
### Ein RGB-Farbcode besteht aus den Farbanteilen Rot, Grün und Blau. Jeder Farbanteil
### kann in der Intensität 0 bis 255 vorliegen. Entwerfen Sie eine Function, die die drei
### Farbanteile dezimal übernimt und den RGB-Farbcode als hexadezimalen Wert
### zurückgibt.
### Beispiel: Übergabewert 168, 128, 252
### Rückgabe: A880FC

### Wir berechnen den entsprechenden Hexwert in einer eigenen Function

def getHex(wert):

    teiler = 16
    ersteStelle = ""
    zweiteStelle = ""

    if wert//teiler > 9:
        ersteStelle = chr(55+wert//teiler)
    else:
        ersteStelle = str(wert//teiler)

    if wert%teiler > 9:
        zweiteStelle = chr(55+wert%teiler)
    else:
        zweiteStelle = str(wert%teiler)

    # Ok, wir schicken die bitfolge an den Aufrufer zurück
    return ersteStelle + zweiteStelle


def f21(r,g,b):

   return getHex(r) + getHex(g) + getHex(b)

# Hauptprogramm

x = int(input("Gib mir die Wertigkeit für ROT  [0...255]: "))
y = int(input("Gib mir die Wertigkeit für GRÜN [0...255]: "))
z = int(input("Gib mir die Wertigkeit für BLAU [0...255]: "))

print("Dein Farbcode lautet: " + f21(x,y,z))