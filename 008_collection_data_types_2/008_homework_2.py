# Есть словарь: d = {‘a’:3, ‘b’:0, ‘c’:4, ‘d’:-3}. Найти самое большое число из значений словаря.


# Главная функция
def main():
    d = {'a':3, 'b':0, 'c':4, 'd':-3}
    a = []
    for i in d:
        a.append(d[i])
    print(f'Самое большое число из словаря d = {d} это {max(a)}')


# Начало программы
if __name__ == '__main__':
    main()