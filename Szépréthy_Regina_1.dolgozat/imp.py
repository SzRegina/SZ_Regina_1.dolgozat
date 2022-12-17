"""Kedves Tanárnő/ Tanár úr / aki javítja!
Remélem, nem probléma, hogy megjelenítéskor az első feladat függvényei lecsúsztak az aljára.
Tehát a 2. feladat eredményei hamarabb szerepelnek, mint az elsőé."""

#1.a
def beker():
    szamkero = int(input("Kérlek, adj meg egy páros számot! "))
    while not szamkero % 2 == 0:
        szamkero = int(input("EZ NEM PÁROS! Páros számot kérek! "))
    else:
        print(szamkero)
#1.b-c.
def beker_kieg():
    harom_egy = int(input("Kérlek, adj meg 3 páros számot! \nKérem az 1. számod: "))
    while not harom_egy % 2 == 0:
        harom_egy = int(input("Ez nem páros! Kérem az 1. számod: "))
    else:
        harom_ketto = int(input("Kérem a 2. számod: "))
        while not harom_ketto % 2 == 0:
            harom_ketto = int(input("Ez nem páros! Kérem az 2. számod: "))
        else:
            harom_harom = int(input("Kérem a 3. számod: "))
            while not harom_harom % 2 == 0:
                harom_harom = int(input("Ez nem páros! Kérem a 3. számod: "))
            else:
                return harom_egy, harom_ketto, harom_harom
"""harom_lista = []
harom_lista.append(beker_kieg())
print(harom_lista[0])"""

#2.a
import random
from random import randint
veletlen = [random.randint(-40, 150) for p in range(0, 13)]
print(f"A lista: {veletlen}")
#2.b
ketjegyu_szamok = 0
for x in veletlen:
    if 10 <= x < 100 and x / 10:
        ketjegyu_szamok += 1
print(f"A kétjegyű számok összege: {ketjegyu_szamok}")
#2.c
result = []
for y in veletlen:
    if y % 2 == 0:
        result.append(y)
print(f"A páros számok összege: {sum(result)}")

#2.d
result2= []
for z in veletlen:
    if z % 2 != 0:
        result2.append(z)
print(f"A páratlan számok összege: {sum(result2)}")
print("*"*10)




