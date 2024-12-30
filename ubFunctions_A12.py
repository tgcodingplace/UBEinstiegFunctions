### UB Umgang mit Functions in Python
#
### Aufgabe 12:
#
### Entwerfen Sie eine Function f7, die alle geraden Zahlen in einem übergebenen Intervall
### ausgibt. Die Intervallgrenzen sind nicht Bestandteil der Ausgabe.

def f7(a, b):

    # Wenn die Intervallgrenze eine gerade Zahl ist erhöhe um 2, denn die Intervallgrenze
    # darf nicht Bestandteil der Ausgabe sein. Erhöhe um 2 auf die nächste gerade Zahl
    # Wäre der Startwert ungerade so erhöhe um 1 auf die nächte gerade Zahl

    if a%2==0:
        a+=2
    else:
        a+=1

    # Startwert ist a, Grenze ist b, erhöhe um 2
    for i in range(a,b,2):
        print(i, end=" ")


# Aufruf im Hauptprogramm

start = int(input("Startwert: "))
ende  = int(input("Endwert  : "))

# Aufruf
f7(start, ende)
