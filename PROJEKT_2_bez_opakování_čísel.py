import random
cisla = set()
tipy = []
i = 0
j = 0
Bulls_pocet = 0
Cows_pocet = 0
chyba_pocet = 0
n = int(input("Vlož počet her: "))
start = int(input("Vlož dolní hranici intervalu: "))
stop = int(input("Vlož horní hranici intervalu: "))

while len(cisla) < n:
    cislo = random.randint(start, stop)
    cisla.add(cislo)

seznam = list(cisla)
print("generovaná čísla: ", seznam)

i = 0
j = 0

for j in range(0, n):
    tip = int(input("Tipni si číslo v mezích dolní a horní hranice: " ))
    tipy.append(tip)
    for i in range(0, n):
        if tipy[j] == seznam[i]:
            if j == i:
                print("Bull na pozici:", i)
                Bulls_pocet = Bulls_pocet + 1
            else: print("Cows na pozici:", i); Cows_pocet = Cows_pocet + 1

print("Bulls: ", Bulls_pocet)
print("Cows: ", Cows_pocet)
