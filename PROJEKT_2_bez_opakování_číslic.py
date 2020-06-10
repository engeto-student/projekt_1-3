import random
cislo = set()
tipy = []
seznam = []

Bulls_pocet = 0
Cows_pocet = 0

i = 0
j = 0

n = int(input("Vlož počet her: "))
m = int(input("Vlož počet číslic: "))

for i in range(0, n):
    for i in range(0, m):
        cislo.clear()
        while len(cislo) < m:
            cislice = str(random.randint(1, 9))
            cislo.add(cislice)
    seznam.append(int("".join(cislo)))

print("Seznam generovaných čísel (pro kontrolu algoritmu): ", seznam)

i = 0
j = 0

for j in range(0, n):
    tip = int(input("Tipni si číslo: " ))
    tipy.append(tip)
    for i in range(0, n):
        if tipy[j] == seznam[i]:
            if j == i:
                print("Bull na pozici:", i)
                Bulls_pocet = Bulls_pocet + 1
            else: print("Cows na pozici:", i); Cows_pocet = Cows_pocet + 1

print("Bulls: ", Bulls_pocet)
print("Cows: ", Cows_pocet)
