### UB Umgang mit Functions in Python
#
### Aufgabe 8:
#
### Entwerfen Sie eine Function f3, die von zwei übergebenen ganzzahligen Werten die
### Summe zurückliefert.


def f3(a, b):

    return a + b

# Aufruf im Hauptprogramm

x = int(input("Eingabe Zahl 1: "))
y = int(input("Eingabe Zahl 2: "))

print("Die Summe aus " + str(x) + " und " + str(y), end = " ")
print("lautet " + str(f3(x,y)))
