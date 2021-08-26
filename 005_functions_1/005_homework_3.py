# Калькулятор
# (поддердивает операции: сложение, вычитание, умножение и деление)


# Функция ввода чисел
def input_numbers(oper, name):
    action = ''
    while True:
        # +
        if oper == '+' and name == 'A':
            action = 'первое слагаемое'
        elif oper == '+' and name == 'B':
            action = 'второе слагаемое'
        # -
        elif oper == '-' and name == 'A':
            action = 'уменьшаемое'
        elif oper == '-' and name == 'B':
            action = 'вычитаемое'
        # *
        elif oper == '*' and name == 'A':
            action = 'первый множитель'
        elif oper == '*' and name == 'B':
            action = 'второй множитель'
        # /
        elif oper == '/' and name == 'A':
            action = 'делимое'
        elif oper == '/' and name == 'B':
            action = 'делитель (не должен равняться 0)'
        x = float(input(f'Введите {action} {name}: '))
        return x


# Функция сложения
def addition(add1, add2):
    print(f'Сумма чисел {add1} + {add2} = {add1 + add2}')


# Функция вычитания
def subtract(add1, add2):
    print(f'Разница чисел {add1} - {add2} = {add1 - add2}')


# Функция умножения
def multi(add1, add2):
    print(f'Произведение чисел {add1} * {add2} = {add1 * add2}')


# Функция деления
def division(add1, add2):
    if not add2:
        print('Ошибка! Делитель равен 0!')
        return
    print(f'Частное чисел {add1} / {add2} = {add1 / add2}')


# Главная функция
def main():
    while True:
        operation = input('Введите желаемую операцию (+, -, *, /, 0 - для выхода)\n')
        if operation == '+' or operation == '-' or operation == '*' or operation == '/':
            a = input_numbers(operation, 'A')
            b = input_numbers(operation, 'B')
            if operation == '+':
                addition(a, b)
            elif operation == '-':
                subtract(a, b)
            elif operation == '*':
                multi(a, b)
            elif operation == '/':
                division(a, b)
        elif operation == '0':
            print('До скорой встречи!')
            break
        else:
            print('Введенное значение операции не соответствует ни одному из допустимых, повторите ввод!')


# Старт программы
if __name__ == '__main__':
    main()