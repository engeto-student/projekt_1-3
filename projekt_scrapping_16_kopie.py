import requests as r
from bs4 import BeautifulSoup as bs
import pandas as pd

URL = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
print(URL)

odpoved_1 = r.get(URL)
soup_1 = bs(odpoved_1.content, "html.parser")
obsah_1 = soup_1.find("div", id='publikace')
radky_1 = obsah_1.find_all("tr")

obec_1 = input("Zadej název města z internetové stránky: ")
print()

i = 0
vyber = 0
poradi = 0
radek_1 = 0

while i < len(radky_1):
    vyber = str(radky_1[i])
    if obec_1 in vyber:
        poradi = i
    elif obec_1 == "Praha":
        poradi = 2
    i += 1

radek_1 = radky_1.__getitem__(poradi)
odkaz_1 = radek_1.find_all("a")[2]
URL = odkaz_1["href"]

URL = "https://volby.cz/pls/ps2017nss/" + URL
print(URL)

odpoved_2 = r.get(URL)
soup_2 = bs(odpoved_2.content, "html.parser")
obsah_2 = soup_2.find("div", id='publikace')
radky_2 = obsah_2.find_all("tr")

obec_2 = input("Zadej název obce z internetové stránky: ")
print()

i = 0
vyber = 0
poradi = 0
while i < len(radky_2):
    vyber = str(radky_2[i])
    if obec_2 in vyber:
        poradi = i
    elif obec_2 == "Praha 18":
        poradi = 11
    elif obec_2 == "Praha 17":
        poradi = 10
    elif obec_2 == "Praha 16":
        poradi = 9
    elif obec_2 == "Praha 15":
        poradi = 8
    elif obec_2 == "Praha 14":
        poradi = 7
    elif obec_2 == "Praha 13":
        poradi = 6
    elif obec_2 == "Praha 12":
        poradi = 5
    elif obec_2 == "Praha 11":
        poradi = 4
    elif obec_2 == "Praha 10":
        poradi = 3
    elif obec_2 == "Praha 1":
        poradi = 2
    i += 1

radek_2 = radky_2.__getitem__(poradi)
odkaz_2 = radek_2.find_all("a")[1]
URL = odkaz_2["href"]

URL = "https://volby.cz/pls/ps2017nss/" + URL
print(URL)
odpoved_3 = r.get(URL)
soup_3 = bs(odpoved_3.content, "html.parser")
obsah_3 = soup_3.find("div", id='publikace')
radky_3 = obsah_3.find_all("tr")


slovnik = {
    "Voliči v seznamu": "",
    "Vydané obálky": "",
    "Volební účast v %": "",
    "Odevzdané obálky": "",
    "Platné hlasy": "",
    "% platných hlasů": ""
}

if "Okrsky" in str(radky_3):
    tabulka = radky_3.__getitem__(2).text
    f = tabulka.splitlines()
    f.remove("")
    f.remove("1")
    f.remove("1")
    f.remove("100,00")
    j = 0
    for i in slovnik:
        slovnik[i] = f[j]
        j += 1
    data_list = list(slovnik.items())
    df = pd.DataFrame(data_list, columns=["klíč", "hodnota"])
    print(df)
    print()

    i = 5
    tab = []
    while i <= 16:
        tabulka_1 = radky_3.__getitem__(i).text
        f_1 = tabulka_1.splitlines()
        f_1.pop(0)
        f_1.pop(0)
        f_1.pop(3)
        f_1.pop(2)
        tab.append(f_1)
        i += 1
    df_1 = pd.DataFrame(tab, columns=["politická strana", "platné hlasy"])
    print(df_1)
    print()

    i = 20
    tab = []
    while i <= 30:
        tabulka_1 = radky_3.__getitem__(i).text
        f_1 = tabulka_1.splitlines()
        f_1.pop(0)
        f_1.pop(0)
        f_1.pop(3)
        f_1.pop(2)
        tab.append(f_1)
        i += 1
    df_2 = pd.DataFrame(tab, columns=["politická strana", "platné hlasy"])
    print(df_2)

else:
    radek = radky_3.__getitem__(1)
    odkaz = radek.find_all("a")
    print("počet okrsků v obci: ", len(odkaz))
    print()
    okrsek = int(input("Vlož číslo okrsku: "))
    URL = odkaz[okrsek - 1]
    URL = URL["href"]
    URL = "https://volby.cz/pls/ps2017nss/" +  URL
    print(URL)
    print()
    odpoved_4 = r.get(URL)
    soup_4 = bs(odpoved_4.content, "html.parser")
    obsah_4 = soup_4.find("div", id='publikace')
    radky_4 = obsah_4.find_all("tr")
    tabulka = radky_4.__getitem__(1).text
    f = tabulka.splitlines()
    f.remove("")
    j = 0
    for i in slovnik:
        slovnik[i] = f[j]
        j += 1
    data_list = list(slovnik.items())
    df_0 = pd.DataFrame(data_list, columns=["klíč", "hodnota"])
    print(df_0)
    print()
    i = 4
    tab = []
    while i <= 15:
        tabulka_1 = radky_4.__getitem__(i).text
        f_1 = tabulka_1.splitlines()
        f_1.pop(0)
        f_1.pop(0)
        f_1.pop(3)
        f_1.pop(2)
        tab.append(f_1)
        i += 1
    df_1 = pd.DataFrame(tab, columns=["politická strana", "platné hlasy"])
    print(df_1)
    print()
    i = 19
    tab = []
    while i <= 29:
        tabulka_1 = radky_4.__getitem__(i).text
        f_1 = tabulka_1.splitlines()
        f_1.pop(0)
        f_1.pop(0)
        f_1.pop(3)
        f_1.pop(2)
        tab.append(f_1)
        i += 1
    df_2 = pd.DataFrame(tab, columns=["politická strana", "platné hlasy"])
    print(df_2)
