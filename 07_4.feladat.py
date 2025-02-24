#4. Feladat
#Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!
def leghosszabb_szo(szavak):
    leghosszab = szavak[0]
    for szo in szavak:
        if len(szo) > len(leghosszab):
            leghosszab = szo
    return leghosszab
szavak = []
for i in range(3):
    szo = input(f'Adj meg egy {i+1}.szót: ')
    szavak.append(szo)
leghosszabb = leghosszabb_szo(szavak)
print(f"A legrövidebb szó: {leghosszabb}")
