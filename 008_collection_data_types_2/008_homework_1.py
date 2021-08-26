# Вывод на экран символов, которые есть в обоих строках


# Главная функция
def main():
    str1 = 'Мама мыла раму'#'Абвгдежз'
    str2 = 'Рыба плавает в море'#'дАБВГДЕЖЗ'

    set1, set2 = set(str1), set(str2)

    set1.intersection_update(set2)

    print(f'Первая строка: {str1}')
    print(f'Вторая строка: {str2}')
    print(f'Символы которые есть в обоих строках: {set1}')


# Начало программы
if __name__ == '__main__':
    main()
