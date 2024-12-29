### UB Umgang mit Functions in Python
#
### Aufgabe 10:
#
### Entwerfen Sie eine Function f5, die von drei übergebenen Zahlenwerten den
### mathematischen Mittelwert zurück liefert.

def f5(a, b, c):

    summe  = a + b + c
    anzahl = 3

    return summe/anzahl

# Aufruf im Hauptprogramm

x = int(input("Eingabe Zahl 1: "))
y = int(input("Eingabe Zahl 2: "))
z = int(input("Eingabe Zahl 2: "))

print("Der mathematische Mittelwert aus " + str(x) + ", " + str(y), end=" ")
print("und " + str(z) + " beträgt " + str(f5(x,y,z)))
