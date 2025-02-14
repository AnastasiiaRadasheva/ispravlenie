from math import *  # importige vajalikud matemaatilised funktsioonid

print("Ruudu karakteristikud")
try:
    a = int(input('Sisesta ruudu külje pikkus => '))
    if type(a) == int and a > 0:
        S = a ** 2  # Pindala
        print("Ruudu pindala", S)
        P = 4 * a  # Ümbermõõt
        print("Ruudu ümbermõõt", P)
        di = a * sqrt(2)  # Diagonaal
        print("Ruudu diagonaal", round(di, 2))
        print()
    else:
        print("Kirjutage number, mitte tähed")  # Kui sisestati vale väärtus
except ValueError:  # Kui sisend ei ole korrektne
    print("Valed andmed")

print("Ristküliku karakteristikud")
try:
    b = int(input("Sisesta ristküliku 1. külje pikkus => "))
    c = int(input("Sisesta ristküliku 2. külje pikkus => "))
    if type(b) == int and b > 0 and type(c) == int and c > 0:
        S = b * c  # Pindala
        print("Ristküliku pindala", S)
        P = 2 * (b + c)  # Ümbermõõt
        print("Ristküliku ümbermõõt", P)
        di = sqrt(b ** 2 + c ** 2)  # Diagonaal
        print("Ristküliku diagonaal", round(di, 2))
        print()
    else:
        print("Kirjutage number, mitte tähed")
except ValueError:  # Kui sisend ei ole korrektne
    print("Valed andmed")

print("Ringi karakteristikud")
try:
    r = float(input("Sisesta ringi raadiusi pikkus => "))  # Raadius
    if type(r) == float and r > 0:
        d = 2 * r  # Läbimõõt
        print("Ringi läbimõõt", d)
        S = pi * r ** 2  # Pindala
        print("Ringi pindala", round(S, 2))
        C = 2 * pi * r  # Ringjoone pikkus
        print("Ringjoone pikkus", round(C, 2))
    else:
        print("Kirjutage andmed õigesti")
except ValueError:  # Kui sisend ei ole korrektne
    print("Valed andmed")
