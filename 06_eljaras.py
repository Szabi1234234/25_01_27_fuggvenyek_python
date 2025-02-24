#2. Feladat
#Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!

def eljaras(szam):
    if szam > 0:
        print('Pozitív')
    elif szam < 0:
        print('Negatív')
    else:
        print('Nullával egyenlö')

input_szam = int(input('Adj meg egy számot: '))

eljaras(input_szam)

while True:
    input_szam = input('Adj meg egy számot: ')
    if input_szam == "":
        break
    szam = int(input_szam) 
    eljaras(szam)