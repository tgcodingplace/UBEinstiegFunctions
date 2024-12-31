### UB Umgang mit Functions in Python
#
### Aufgabe 19:
#
### Entwerfen Sie eine Function f13, die einen mathematischen Ausdruck auswertet. Das
### berechnete Ergebnis soll als vollständige Gleichung zurückgegeben werden. Wir
### beschränken uns aus zwei Zahlen und auf die Operatoren +, -, *, /, % und //.
### Beispiel: Übergabe: 5, 8, „+“
### Rückgabe: 5 + 8 = 13

def f13(a, b, c):

    ausgabe = ""

    if c == "+":
        ausgabe = str(a) + " + " + str(b) + " = " + str(a+b)

    if c == "-":
        ausgabe = str(a) + " - " + str(b) + " = " + str(a-b)

    if c == "*":
        ausgabe = str(a) + " * " + str(b) + " = " + str(a*b)

    if c == "/":
        ausgabe = str(a) + " / " + str(b) + " = " + str(a/b)

    if c == "%":
        ausgabe = str(a) + " % " + str(b) + " = " + str(a%b)

    if c == "//":
        ausgabe = str(a) + " // " + str(b) + " = " + str(a//b)

    return ausgabe

# Aufruf im Hauptprogramm

x = int(input("Gib mir eine erste Zahl : "))
y = int(input("Gib mir eine zweite Zahl: "))
z = input("Gib mir eine mathematische Operation [+, -, *, /, //, %]: ")

print(f13(x,y,z))
