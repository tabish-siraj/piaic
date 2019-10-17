from funs import funs

func = funs()

while True:
    act = int(input('''
    Please Select Operation:
    1. Add Word
    2. Human to Alien
    3. Alient to Human
    4. Exit\n
    '''))
    if act == 1:
        func.addWord()
    elif act == 2:
        func.humanToAlien()
    elif act == 3:
        func.alienToHuman()
    elif act == 4:
        break