#A "Próbáld ki!" gombra kattintva elérhető egy program, ami egy eljárás segítségével kirajzol a 
# képernyőre egy 6x3-as mezőt. Alakítsd át ezt a programot úgy, az eljárás hívásakor megadott értékpárnak megfelelően a program az adott 
#pozícióba 'O' helyett '+' jelet írjon ki. A lenti példában az eljárás hivása: mezot_rajzol(0,4)
def mezot_rajzol():
	for sor in range(3):
		for oszlop in range(6):
			print('O ', end='')
		print()

mezot_rajzol()
x = input('Adj meg egy számot vizszintesen: ')
y = input('Adj meg egy számot fuggőlegesen: ')

def mezot_rajzol(x, y):
    for sor in range(3):
        for oszlop in range(6):
            if oszlop == y or sor == x:
                print('O ', end='')
            else:
                print('+ ', end='')
        print()