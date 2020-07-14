deska = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

hraci_pole = list(deska)

def intro():
    print("PRAVIDLA HRY PIŠKVORKY:")
    print("""Hrací desku tvoří 9 polí.
Hráč s křížkem začíná hru.
Hráči se ve svých tazích střídají. 
Hráč je na tahu poté, když jeho soupeř provedl tah.
Cílem obou hráčů je vytvořit nepřerušenou vodorovnou, 
svislou nebo šikmou řadu tří křížků nebo koleček. """)

intro()
print()

def zobraz_desku(deska):
    print("Hrací pole:")
    print()
    print(deska['1'] + '|' + deska['2'] + '|' + deska['3'])
    print('-----')
    print(deska['4'] + '|' + deska['5'] + '|' + deska['6'])
    print('-----')
    print(deska['7'] + '|' + deska['8'] + '|' + deska['9'])
    print()

def hra():
    na_tahu = 'X'
    pocet = 0

    i = 0
    while i > -1:
        zobraz_desku(deska)
        print("Jsi na řadě,", na_tahu)
        kod = ""

        j = 0
        while j > -1:
            kod = input("Vlož číselný kód i - tého pole od 1 do 9: ")
            print()
            if kod not in hraci_pole:
                print("jsi mimo herní plochu")
            else: break
            j += 1

        if deska[kod] == ' ':
            deska[kod] = na_tahu
            pocet += 1
        else:
            print("Místo je vyplněno, vyber si jiné.")
            continue

        if i >= 5:
            if deska['1'] == deska['2'] == deska['3'] != ' ':
                zobraz_desku(deska)
                print("Hra skončila.")
                print(na_tahu, "zvítězil")
                break
            elif deska['4'] == deska['5'] == deska['6'] != ' ':
                zobraz_desku(deska)
                print("Hra skončila.")
                print(na_tahu, "zvítězil")
                break
            elif deska['7'] == deska['8'] == deska['9'] != ' ':
                zobraz_desku(deska)
                print("Hra skončila.")
                print(na_tahu, "zvítězil")
                break
            elif deska['1'] == deska['4'] == deska['7'] != ' ':
                zobraz_desku(deska)
                print("Hra skončila.")
                print(na_tahu, "zvítězil")
                break
            elif deska['2'] == deska['5'] == deska['8'] != ' ':
                zobraz_desku(deska)
                print("Hra skončila.")
                print(na_tahu, "zvítězil")
                break
            elif deska['3'] == deska['6'] == deska['9'] != ' ':
                zobraz_desku(deska)
                print("Hra skončila.")
                print(na_tahu, "zvítězil")
                break
            elif deska['7'] == deska['5'] == deska['3'] != ' ':
                zobraz_desku(deska)
                print("Hra skončila.")
                print(na_tahu, "zvítězil")
                break
            elif deska['1'] == deska['5'] == deska['9'] != ' ':
                zobraz_desku(deska)
                print("Hra skončila.")
                print(na_tahu, "zvítězil")
                break

        if pocet == 9:
            deska[kod] = na_tahu
            zobraz_desku(deska)
            print("Hra skončila.")
            print("Nikdo nevyhrál.")
            break

        if na_tahu == 'X':
            na_tahu = 'O'
        else:
            na_tahu = 'X'
        i += 1
hra()
