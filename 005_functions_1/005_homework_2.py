# Поиск наибольшего общего делителя для двух целых чисел


# Функция ввода чисел
def input_numbers(name):
    while True:
        x = float(input(f'Введите целое число {name}: '))
        if not x % 1:
            return x
        else:
            print('Введенное число не является целым, повторите ввод!')


# Функция поиска наибольшего общего делителя
def finder(a, b):
    finish = abs(b)
    res = 1
    if a > b:
        finish = abs(a)
    for i in range(2, finish+1):
        if not a % i and not b % i:
            res = i
    return res


# Главная функция
def main():
    a = input_numbers('A')
    b = input_numbers('B')
    result = finder(a, b)
    print(f'Общий делитель для чисел {a} и {b} = {result}')


# Старт программы
if __name__ == '__main__':
    main()