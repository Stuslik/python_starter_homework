print('Рисуем на экране прямоугольный треугольник указанной пользователем высоты\n')
print('Виды треугольников:')
print(' 1 или 2 или 3 или 4 ')
print('*       *   ***   ***')
print('**     **   **     **')
print('***   ***   *       *')

tip = 0
while tip < 1 or tip > 4:
    tip = int(input('Выберите вид рисуемого треугольника, один из 4-х: '))
th = 0
while th <= 1:
    th = int(input('Введите высоту треугольника (>1): '))
symbol = ''
while len(symbol) != 1:
    symbol = input('Выберите символ для рисования треугольника:')
# 1
print()
if tip == 1:
    print('For:')
    for row in range(0, th):
        for col in range(0, th):
            if row >= col:
                print(symbol, end='')
            else:
                print(' ', end='')
        print()
    print('While:')
    row = 1
    col = 1
    while row <= th:
        while col <= th:
            if row >= col:
                print(symbol, end='')
            else:
                print(' ', end='')
            col += 1
        print()
        col = 1
        row += 1
# 2
elif tip == 2:
    print('For:')
    for row in range(0, th):
        for col in range(th - 1, -1, -1):
            if row >= col:
                print(symbol, end='')
            else:
                print(' ', end='')
        print()
    print('While:')
    row = 1
    col = th
    while row <= th:
        while col >= 1:
            if row >= col:
                print(symbol, end='')
            else:
                print(' ', end='')
            col -= 1
        print()
        col = th
        row += 1
# 3
elif tip == 3:
    print('For:')
    for row in range(0, th):
        for col in range(th - 1, -1, -1):
            if row <= col:
                print(symbol, end='')
            else:
                print(' ', end='')
        print()
    print('While:')
    row = 1
    col = th
    while row <= th:
        while col >= 1:
            if row <= col:
                print(symbol, end='')
            else:
                print(' ', end='')
            col -= 1
        print()
        col = th
        row += 1
# 4
elif tip == 4:
    print('For:')
    for row in range(0, th):
        for col in range(0, th):
            if row <= col:
                print(symbol, end='')
            else:
                print(' ', end='')
        print()
    print('While:')
    row = 1
    col = 1
    while row <= th:
        while col <= th:
            if row <= col:
                print(symbol, end='')
            else:
                print(' ', end='')
            col += 1
        print()
        col = 1
        row += 1