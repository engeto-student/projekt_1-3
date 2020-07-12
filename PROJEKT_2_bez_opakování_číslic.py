import random
numbers = set()
tips = []
list = []

Bulls_pocet = 0
Cows_pocet = 0

n = int(input("Vlož počet her: "))
m = int(input("Vlož počet číslic: "))

for i in range(0, n):
    for i in range(0, m):
        numbers.clear()
        while len(numbers) < m:
            cislice = str(random.randint(1, 9))
            numbers.add(cislice)
    list.append(int("".join(numbers)))

print("Seznam generovaných čísel (pro kontrolu algoritmu): ", list)

for j in range(0, n):
    tip = int(input("Tipni si číslo: " ))
    tips.append(tip)
    for i in range(0, n):
        if tips[j] == list[i]:
            if j == i:
                print("Bull na pozici:", i)
                Bulls_pocet = Bulls_pocet + 1
                print("Bulls: ", Bulls_pocet)
                print("Cows: ", Cows_pocet)
            else: print("Cows na pozici:", i); Cows_pocet = Cows_pocet + 1; print("Bulls: ", Bulls_pocet); print("Cows: ", Cows_pocet)

    if tips[j] not in list:
        print("Tipované číslo není mezi čísly generovanými.")
        print("Bulls celkem: ", Bulls_pocet)
        print("Cows celkem: ", Cows_pocet)
