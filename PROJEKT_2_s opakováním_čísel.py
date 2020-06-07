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
print("generovaaná čísla (pro kontrolu funkčnosti programu): ", cisla)

i = 0
j = 0

for j in range(0, n):
    tip = int(input("Tipni si číslo v mezích dolní a horní hranice intervalu: " ))
    tipy.append(tip)
    for i in range(0, n):
        if tipy[j] == cisla[i]:
            if j == i:
                print("Bull na pozici:", i)
                Bulls_pocet = Bulls_pocet + 1
            else: print("Cows na pozici:", i); Cows_pocet = Cows_pocet + 1

print("Bulls: ", Bulls_pocet)
print("Cows: ", Cows_pocet)

'''Tvým úkolem bude vytvořit program, který by simuloval hru Bulls and Cows. Hra funguje následovně:

Počítač vygeneruje tajné 4 místné číslo. Každá číslice tohoto čísla musí být jiná.
Počítač vždy vyzve uživatele, aby hádal toto číslo.
Počítač vyhodnotí tip uživatele a vrátí počty shod.
Pokud uživatel uhádne správné číslo i správnou pozici, jedná se o "bulls". Pokud je pozice jiná, ale číslice je správná,
jedná se o "cows".'''

'''Příklad hry s číslem 2017
Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Enter a number
>>> 1234
0 bulls, 2 cows
>>> 6147
1 bull, 1 cow
>>> 2417
3 bulls, 0 cows
>>> 2017
Correct, you've guessed the right number in 4 guesses!
That's {amazing, average, not so good, ...}'''