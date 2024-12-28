### UB Umgang mit Functions in Python
#
### Aufgabe 6:
#
### Entwerfen Sie eine Function f1, die von einem übergebenen ganzzahligen Wert überprüft,
### ob sie gerade ist oder nicht. Geben Sie einen boolschen Wert zurück.
#

def f1(wert):

    # % --> Modulo = Restwetrtoperator
    if wert%2==0:
        return True
    
    return False

# Aufruf im Hauptprogramm

eingabe = int(input("Eingabe einer Ganzzahl: "))

# wahr oder falsch wird ausgewertet
if f1(eingabe):
    print(str(eingabe) + " ist gerade ")
else:
    print(str(eingabe) + " ist ungerade ") 