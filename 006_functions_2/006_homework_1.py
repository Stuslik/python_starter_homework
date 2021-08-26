# Замена значения глобальной переменной


# Замена глобальной переменной
def change_global():
    global var
    var = 52


# Главная функция
def main():
    global var
    print(var)
    change_global()
    print(var)


# Начало программы
var = 37
if __name__ == '__main__':
    main()
