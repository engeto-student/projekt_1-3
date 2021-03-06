
uzivatel = ("bob", "ann", "mike", "liz")
heslo = ('123', 'pass123', 'password123', 'pass')

'''
| USER |   PASSWORD  |
------------------------------
| bob  |     123     |
| ann  |    pass123  |
| mike | password123 |
| liz  |    pass123  |
'''

pocet_uzivatelu = len(uzivatel)
pokusy = 3

i = 0
j = 0

while i < pokusy:
    uz = input("Vlož své uživatelské jméno: ")
    hes = input("Vlož své heslo: ")
    if uz in uzivatel and hes in heslo:
        print("Vstupní jméno a heslo jsou správné, můžete pokračovat do systému.")
        break
    i += 1
else: print("Chybné jméno nebo heslo, přístup do systému byl zamítnut."), exit()

TEXTS = [''' Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick. ''',

''''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

print("Počet textů v souboru: ", len(TEXTS))

i = 0
slovnik = dict()

while i < len(TEXTS):
    slovnik[i] = TEXTS[i]
    i += 1

x = int(input("Vlož číslo od 0 do 2: "))

rozdeleni = slovnik.get(x).split()
print("text: ", rozdeleni)
pocet_slov = len(rozdeleni)
print("Celkový počet slov: ", pocet_slov)

i = 0
pocet_slov_PVP = 0
pocet_slov_VP = 0
pocet_slov_MP = 0
pocet_cisel = 0

while i < pocet_slov:
    if rozdeleni[i].istitle():
        pocet_slov_PVP = pocet_slov_PVP + 1
    if rozdeleni[i].isupper():
        pocet_slov_VP = pocet_slov_VP + 1
    if rozdeleni[i].islower():
        pocet_slov_MP = pocet_slov_MP + 1
    if rozdeleni[i].isdigit():
        pocet_cisel = pocet_cisel + 1
    i += 1

print("Slova s počátečním VP: ", pocet_slov_PVP)
print("Slova psaná velkými písmeny: ", pocet_slov_VP)
print("Slova psaná malými písmeny: ", pocet_slov_MP)
print("Počet cisel: ", pocet_cisel)

i = 0
j = 0
delka_slova = 0
pocet_pismen = 0

while i < pocet_slov:
    while j < pocet_slov:
        delka_slova = len(rozdeleni[j])
        if delka_slova == i:
            pocet_pismen = pocet_pismen + 1
            print(i, "se vyskytuje: ", pocet_pismen )
        j += 1
    i += 1

i = 0
max = len(rozdeleni[i])

while i < pocet_slov:
    if i > 0:
        if len(rozdeleni[i]) > max:
            max = len(rozdeleni[i])
    i += 1

i = 0
delka_slova = 0
suma = 0

while i <= max:
    j = 0
    pocet = 0
    while j < pocet_slov:
        delka_slova = len(rozdeleni[j])
        if delka_slova == i:
            pocet = pocet + 1
        j += 1
    print(i, "se vyskytuje:", pocet, "krát", "*" * pocet )
    i += 1

i = 0
suma = 0

while i < pocet_slov:
    if rozdeleni[i].isdigit():
        suma = suma + int(rozdeleni[i])
    i += 1
print("Součet čísel v textu: ", suma)

