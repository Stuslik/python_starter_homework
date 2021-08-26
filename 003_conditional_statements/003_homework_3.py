import math
print('Простенький калькулятор')
print('поддерживает следующие операции:')
print('+, -, *, /, **, sin, cos, tan')
print('Предупреждение, на запрос о вводе числа, вводить исключительно число, а не строку!')
operation = input('Введите тип желаемой операции: ')
if operation == '+' or operation == '-' or operation == '*' or operation == '/' or operation == '**':
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    # хорошо бы добавить проверку на ввод чисел, а не строк
    if operation == '+':
        print(f'{a} + {b} = {a + b}')
    if operation == '-':
        print(f'{a} - {b} = {a - b}')
    if operation == '*':
        print(f'{a} * {b} = {a * b}')
    if operation == '/':
        print(f'{a} / {b} = {a / b}')
    if operation == '**':
        print(f'{a} ** {b} = {a ** b}')
elif operation == 'sin' or operation == 'cos' or operation == 'tan':
    a = float(input('Введите число: '))
    # хорошо бы добавить проверку на ввод числа, а не строки
    if operation == 'sin':
        print(f'sin({a}) = {round(math.sin(a), 2)}')
    if operation == 'cos':
        print(f'cos({a}) = {round(math.cos(a), 2)}')
    if operation == 'tan':
        print(f'tan({a}) = {round(math.tan(a), 2)}')
else:
    print('Введена не правильная операция!')