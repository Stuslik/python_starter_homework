# Ввод текста с клавиатуры. Вывод отсортированных по алфавиту слов данного текста
# Рекомендуется вводить текст в одном регистре, так как он все равно будет приведен к строчному виду


# Функция замены перечисленных символов на ничего
def replace_symbols(text):
    # Перечень заменяемых символов
    symbols = ['.', ',', '!', '?', '-', '+', '*', '/', '<', '>', '—', '"', "'"]
    for i in symbols:
        text = text.replace(i, '')
    return text


# Функция создания списка
def create_list(text):
    list_no_sorted = replace_symbols(text).split()
    return list_no_sorted


# Функция вывода на экран
def list_to_screen(list_sorted):
    # Если хотим вывести каждое слово на отдельной строке
    for i in list_sorted:
        print(i)
    # Если хотим вывести целиком список
    #print(list_sorted)


# Главная функция
def main():
    string = input('Введите текст:\n')
    list_sorted = create_list(string.lower())
    list_sorted.sort()
    list_to_screen(list_sorted)


# Начало программы
if __name__ == '__main__':
    main()