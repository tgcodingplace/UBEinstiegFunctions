### UB Umgang mit Functions in Python
#
### Aufgabe 14:
#
### Entwerfen Sie eine Function f8, die alle ganzzahligen Werte eines übergebenen Intervalls
### aufaddiert. Die Summe wird zurückgegeben.

def f8(a, b):

    # In diese lokale Variable schreiben wir die Zahlenreihe
    summe = 0

    # In diesem Fall gehören die Intervallgrenzen dazu.
    # Wäre der Startwert ungerade so erhöhe um 1 auf die nächste gerade Zahl

    if a%2==1:
        a+=1
    
    # Startwert ist a, Grenze ist b+1 - warum? Angenommen b wäre eine gerade Zahl,
    # dann würde b nicht mehr berücksichtig werden, daher b + 1, erhöhe um 2
    # Summiere alle geraden Zahlenwerte auf
    for i in range(a,b+1,2):
        summe+=i

    # Ok, wir schicken die in summe abgelegte Zahl an den Aufrufer
    # zurück
    return summe


# Aufruf im Hauptprogramm

start = int(input("Startwert: "))
ende  = int(input("Endwert  : "))

# Aufruf und Ausgabe des Rückgabewertes
print(f8(start, ende))