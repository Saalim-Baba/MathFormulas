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
        Startkapital, Jahre = inputs
        Abschreibungsprozentsatz = float(input("Abschreibungsprozentsatz: "))
        for jahr in range(1, Jahre + 1):
            Abschreibungsbetrag = Startkapital * (Abschreibungsprozentsatz / 100)
            Startkapital -= Abschreibungsbetrag
            print(f"Jahr {jahr}: Buchwert = {Startkapital}, Abschreibung = {Abschreibungsbetrag}")
    else:
        print("Ungültige Auswahl.")


def renten_formel():
    renten_choice = int(input("Was gesucht?\n\tEndwert(1)\n\tBarwert(2)\n\tRente vom Barwert(3)\n\tRente vom Endwert("
                              "4)\n\tJahre(5)\nEingabe: "))
    vorschuessig = input("Vorschüssig? (Ja/Nein): ")
    quest = ["Endwert: ", "Barwert: ", "Rente: ", "Jahre: "]
    inputs = []

    for q in range(len(quest)):
        if q + 1 == renten_choice:
            continue
        value = float(input(quest[q]))
        inputs.append(value)

    if vorschuessig.lower() == "Ja":
        n = int(input("Anzahl der Zinsperioden pro Jahr: "))
    else:
        print("Es wird nachschüssig automatisch benutzt")
        n = 1

    def vorschuessig():
        pass



    def nachschuessig():
        Rente, Zinsfaktor, Jahre = inputs
        print(f"Endwert: {Rente * ((Zinsfaktor ** Jahre - 1) / (Zinsfaktor - 1))}")



if __name__ == '__main__':
    print("Willkommen zu den Mathe formeln\n")
    choice = input("Was möchten Sie?\nMitternachtsformel(M)\nZins_formel(Z)\nRenten_formel(R)\n\nEingabe: ")
    if choice == "M":
        mitternachtsformel()
    if choice == "Z":
        zins_formel()
    if choice == "R":
        renten_formel()
