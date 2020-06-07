import random
cislo = set()
tipy = []
podseznam = []
seznam = []

podseznam_1 = 0
podseznam_2 = 0
podseznam_3 = 0
podseznam_4 = 0

Bulls_pocet = 0
Cows_pocet = 0

i = 0
j = 0

n = int(input("Vlož počet her: "))

for i in range(0, n):
    cislo.clear()
    while len(cislo) < n:
        cislice = random.randint(1, 9)
        cislo.add(cislice)
    podseznam = list(cislo)
    suma = 0
    for i in range(0, n):
        if i == 0:
            podseznam_1 = podseznam[i] * 1000
        elif i == 1:
            podseznam_2 = podseznam[i] * 100
        elif i == 2:
            podseznam_3 = podseznam[i] * 10
        else:
            podseznam_4 = podseznam[i] * 1
    suma = suma + podseznam_1 + podseznam_2 + podseznam_3 + podseznam_4
    seznam.append(suma)
print("Seznam generovaných čísel: ", seznam)

i = 0
j = 0

for j in range(0, n):
    tip = int(input("Tipni si číslo v intervalu 1 000 - 9 999: " ))
    tipy.append(tip)
    for i in range(0, n):
        if tipy[j] == seznam[i]:
            if j == i:
                print("Bull na pozici:", i)
                Bulls_pocet = Bulls_pocet + 1
            else: print("Cows na pozici:", i); Cows_pocet = Cows_pocet + 1

print("Bulls: ", Bulls_pocet)
print("Cows: ", Cows_pocet)

