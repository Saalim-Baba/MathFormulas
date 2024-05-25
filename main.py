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

    def renten_rechnung(inputs):
        Zinsfaktor, *rest = inputs
        Zinsfaktor = Zinsfaktor / 100 + 1

        if renten_choice == 1:
            Jahre, Rente = rest
            Endwert = Rente * ((Zinsfaktor ** Jahre - 1) / (Zinsfaktor - 1))
            return Endwert

        elif renten_choice == 2:
            Jahre, Rente = rest
            Barwert = Rente * ((Zinsfaktor ** Jahre - 1) / (Zinsfaktor ** Jahre) * (Zinsfaktor - 1))
            return Barwert

        elif renten_choice == 3:
            Jahre, Barwert = rest
            rente_von_barwert = Barwert * ((Zinsfaktor ** Jahre * (Zinsfaktor - 1) / (Zinsfaktor ** Jahre - 1)))
            return rente_von_barwert

        elif renten_choice == 4:
            Jahre, Endwert = rest
            rente_von_endwert = Endwert * ((Zinsfaktor - 1) / (Zinsfaktor ** Jahre - 1))
            return rente_von_endwert

        elif renten_choice == 5:
            Rente, Endwert = rest
            Jahre = math.log(((Endwert * (Zinsfaktor - 1)) / Rente) + 1) / math.log(Zinsfaktor)
            return Jahre

        else:
            return "Fail"

    renten_choice = int(input("Was gesucht?\n\tEndwert(1)\n\tBarwert(2)\n\tRente vom Barwert(3)\n\tRente vom Endwert("
                              "4)\n\tJahre(5)\nEingabe: "))
    vorschuessig = input("Vorschüssig? (Ja/Nein): ")

    quest = ["Zinsfaktor: ", "Jahre: "]
    if renten_choice == 5:
        quest.remove("Jahre: ")
    if renten_choice in (1, 2, 5):
        quest.append("Rente: ")
    if renten_choice == 3:
        quest.append("Barwert: ")
    if renten_choice in (4, 5):
        quest.append("Endwert: ")

    inputs = []
    print(len(quest))
    for q in range(len(quest)):
        value = float(input(quest[q]))
        inputs.append(value)

    if vorschuessig.lower() == "ja":
        renten_rechnung(inputs)
    else:
        print(round(renten_rechnung(inputs), 2))


if __name__ == '__main__':
    print("Willkommen zu den Mathe formeln\n")
    choice = input("Was möchten Sie?\nMitternachtsformel(M)\nZins_formel(Z)\nRenten_formel(R)\n\nEingabe: ")
    if choice == "M":
        mitternachtsformel()
    if choice == "Z":
        zins_formel()
    if choice == "R":
        renten_formel()
