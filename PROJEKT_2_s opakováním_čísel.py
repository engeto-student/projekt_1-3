import random
cisla = []
tipy = []
i = 0
j = 0
Bulls_pocet = 0
Cows_pocet = 0
chyba_pocet = 0
n = int(input("Vlož počet her: "))
start = int(input("Vlož dolní hranici intervalu: "))
stop = int(input("Vlož horní hranici intervalu: "))

for i in range(0, n):
    cislo = random.randint(start, stop)
    cisla.append(cislo)
print("generovaná čísla (pro kontrolu funkčnosti programu): ", cisla)

for j in range(0, n):
    tip = int(input("Tipni si číslo v mezích dolní a horní hranice intervalu: " ))
    tipy.append(tip)
    for i in range(0, n):
        if tipy[j] == cisla[i]:
            if j == i:
                print("Bull na pozici:", i)
                Bulls_pocet = Bulls_pocet + 1
                print("Bulls celkem: ",Bulls_pocet)
                print("Cows celkem: ", Cows_pocet)
            else: print("Cows na pozici:", i); Cows_pocet = Cows_pocet + 1; print("Bulls celkem: ",Bulls_pocet), \
                                                                            print("Cows celkem: ", Cows_pocet)
    if tipy[j] not in cisla:
        print("Tipované číslo není mezi čísly generovanými.")
        print("Bulls celkem: ", Bulls_pocet)
        print("Cows celkem: ", Cows_pocet)

