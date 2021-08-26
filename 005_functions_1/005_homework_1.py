# Приветствие с заданным именем


# Функция ввода имени
def input_name():
    name = input('Введите свое имя: ')
    return name


# Функция приветствия
def hello(name = 'Сергей'):
    print(f'Привет {name}!')


# Главная функция
def main():
    name = input_name()
    if name:
        hello(name)
    else:
        hello()


# Старт программы
if __name__ == '__main__':
    main()