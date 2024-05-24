import math
from math import sqrt


def mitternachtsformel():
    try:
        a = float(input("a:  "))
        b = float(input("b:  "))
        c = float(input("c:  "))
        res = (b ** 2) - (4 * (a * c))
        x1 = (-b + sqrt(res)) / (2 * a)
        x2 = (-b - sqrt(res)) / (2 * a)
        print(round(x1, 2))
        print(round(x2, 2))
    except ValueError:
        print("Fail")


def zins_formel():
    choice = int(input("Was gesucht?\n\tStartkapital(1)\n\tEndkapital(2)\n\tZinssatz(3)\n\tJahre(4)\n\tDegressive "
                       "Abschreibung(5)\nEingabe: "))
    unterjaehrige_verzinsung = input("Unterjährige Verzinsung? (ja/nein): ")
    quest = ["Startkapital: ", "Endkapital: ", "Zinssatz: ", "Jahre: "]
    inputs = []

    for q in range(len(quest)):
        if q + 1 == choice:
            continue
        value = float(input(quest[q]))
        inputs.append(value)

    if unterjaehrige_verzinsung.lower() == "ja":
        n = int(input("Anzahl der Zinsperioden pro Jahr: "))
    else:
        n = 1

    if choice == 2:
        Startkapital, Zinssatz, Jahre = inputs
        Endkapital = Startkapital * (1 + (Zinssatz / 100) / n) ** (n * Jahre)
        print(f"Endkapital: {Endkapital}")
    elif choice == 1:
        Endkapital, Zinssatz, Jahre = inputs
        Startkapital = Endkapital / ((1 + (Zinssatz / 100) / n) ** (n * Jahre))
        print(f"Startkapital: {Startkapital}")
    elif choice == 3:
        Startkapital, Endkapital, Jahre = inputs
        Zinssatz = n * ((Endkapital / Startkapital) ** (1 / (n * Jahre)) - 1) * 100
        print(f"Zinssatz: {Zinssatz}%")
    elif choice == 4:
        Startkapital, Endkapital, Zinssatz = inputs
        Jahre = math.log(Endkapital / Startkapital) / (n * math.log(1 + (Zinssatz / 100) / n))
        print(f"Jahre: {round(Jahre, 2)}")
    elif choice == 5:
        Anschaffungswert = float(input("Anschaffungswert: "))
        Abschreibungsprozentsatz = float(input("Abschreibungsprozentsatz: "))
        Nutzungsdauer = int(input("Nutzungsdauer (Jahre): "))
        for jahr in range(1, Nutzungsdauer + 1):
            Abschreibungsbetrag = Anschaffungswert * (Abschreibungsprozentsatz / 100)
            Anschaffungswert -= Abschreibungsbetrag
            print(f"Jahr {jahr}: Buchwert = {Anschaffungswert}, Abschreibung = {Abschreibungsbetrag}")
    else:
        print("Ungültige Auswahl.")


def renten_formel():
    choice = int(input("Was gesucht?\n\tEndwert(1)\n\tBarwert(2)\n\tRente vom Barwert(3)\n\tRente vom Endwert("
                       "4)\n\tJahre(5)\nEingabe: "))
    vorschuessig = input(" vorschüssig? (ja/nein): ")
    quest = ["Startkapital: ", "Endkapital: ", "Zinssatz: ", "Jahre: "]
    inputs = []

    for q in range(len(quest)):
        if q + 1 == choice:
            continue
        value = float(input(quest[q]))
        inputs.append(value)

    if vorschuessig.lower() == "ja":
        n = int(input("Anzahl der Zinsperioden pro Jahr: "))
    else:
        print("Es wird nachschüssig automatisch benutzt")
        n = 1


if __name__ == '__main__':
    print("Willkommen zu den Mathe formeln\n")
    choc = input("Was möchten Sie?\nmitternachtsformel(M)\nzins_formel(Z)\nrenten_formel(R)\n\nEingabe: ")
    if choc == "M":
        mitternachtsformel()
    if choc == "Z":
        zins_formel()
    if choc == "R":
        renten_formel()
