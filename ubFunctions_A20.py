### UB Umgang mit Functions in Python
#
### Aufgabe 20:
#
### Entwerfen Sie eine Function f14, die ein übergebenes Passwort auf Sicherheit überprüft.
### Wir legen für diese Aufgabe fest, dass ein gutes Passwort eine Mindestlänge von 10
### Zeichen haben soll. Weiterhin wird verlangt, dass es mindestens 2 Zahlen, 2
### Sonderzeichen, 2 Kleinbuchstaben und 2 Großbuchstaben beinhalten soll.
### Geben Sie zurück, ob das eingegebene Passwort die Kriterien erfüllt oder nicht.

### Natürlich geht das auch alles auf einen Rutsch. Wir legen aber für das bessere
### Verständnis für jedes Kriterium eine eigene Function an

def checkLaenge(pw):

    laenge = 0
    for i in pw:
        laenge+=1
    return laenge > 9

def istZahl(c):
    # Ganzzahlen besitzen ASCII-Codes von 48 bis 57 ( 0...9)
    return ord(c) >= 48 and ord(c) <= 57

def istGrossbuchstabe(c):
    # Ganzzahlen besitzen ASCII-Codes von 65 bis 90 ( A...Z )
    return ord(c) >= 65 and ord(c) <= 90

def istKleinbuchstabe(c):
    # Kleinbuchstaben besitzen ASCII-Codes von 97 bis 122 ( a...z )
    return ord(c) >= 97 and ord(c) <= 122

def istSonderzeichen(c):
    
    # wenn es kein Grossbuchstabe, kein Kleinbuchstabe und keine Zahl ist
    # dann muss es ein Sonderzeichen sein    
    pruefung = not istGrossbuchstabe(c)
    pruefung = pruefung and (not istKleinbuchstabe(c))
    pruefung = pruefung and (not istZahl(c))

    return pruefung

def f20(p):

    laenge = checkLaenge(p) 
    
    anzahlGrossBuchstaben = 0
    anzahlKleinBuchstaben = 0
    anzahlZahlen = 0
    anzahlSonderzeichen = 0

    for i in p:

        if istGrossbuchstabe(i):
            anzahlGrossBuchstaben+=1

        if istKleinbuchstabe(i):
            anzahlKleinBuchstaben+=1
            
        if istZahl(i):
            anzahlZahlen+=1

        if istSonderzeichen(i):
            anzahlSonderzeichen+=1

    check = laenge and anzahlGrossBuchstaben > 1
    check = check and anzahlKleinBuchstaben > 1
    check = check and anzahlSonderzeichen > 1
    check = check and anzahlZahlen > 1

    return check

# Hauptprogramm

print("Hier sind die Kriterien für ein Dein Passwort:")
print()
print("Mindestlänge 10 Zeichen")
print("2x Grossbuchstabe")
print("2x Kleinbuchstabe")
print("2x Zahl")
print("2x Sonderzeichen")
print()

mypass = input("Teste Dein Passwort: ")

print("Test bestanden: " + str(f20(mypass)))

