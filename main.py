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
    choice = int(input("Was gesucht?\n\tStartkapital(1)\n\tEndkapital(2)\n\tZinssatz(3)\n\tJahre(4)\nEingabe:"))
    quest = ["Startkapital: ", "Endkapital: ", "Zinssatz: ", "Jahre: "]
    inputs = []

    for q in range(len(quest)):
        if q + 1 == choice:
            continue
        value = float(input(quest[q]))
        inputs.append(value)

    if choice == 2:
        Startkapital, Zinssatz, Jahre = inputs
        Endkapital = Startkapital * (1 + Zinssatz / 100) ** Jahre
        print(f"Endkapital: {Endkapital}")
    elif choice == 1:
        Endkapital, Zinssatz, Jahre = inputs
        Startkapital = Endkapital / ((1 + Zinssatz / 100) ** Jahre)
        print(f"Startkapital: {Startkapital}")
    elif choice == 3:
        Startkapital, Endkapital, Jahre = inputs
        Zinssatz = (Endkapital / Startkapital) ** (1 / Jahre) - 1
        print(f"Zinssatz: {Zinssatz * 100}%")
    elif choice == 4:
        Startkapital, Endkapital, Zinssatz = inputs
        Jahre = (math.log(Endkapital / Startkapital) / math.log(1 + Zinssatz / 100))
        print(f"Jahre: {round(Jahre, 2)}")
    else:
        print("Ungültige Auswahl.")


if __name__ == '__main__':
    print("Willkommen zu den Matheformeln\n")
    choc = input("Was möchten Sie?\nmitternachtsformel\nzins_formel\n\nEingabe: ")
    if choc == "M":
        mitternachtsformel()
    if choc == "Z":
        zins_formel()
