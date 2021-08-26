# Проверка слова на палиндром
# Если выйти за рамки изучаемого материала
# и использовать списки и методы upper() или lower() для приведения всех букв к одному регистру,
# а так же replace() для того чтобы убрать пробелы, точки, запятые, и прочие знаки и символы
# то можно сделать универсальную программу проверки на палиндром
# В противном случае будет проверка только одного слова написанного в одном регистре


# Функция замены перечисленных символов на ничего
def replace_symbols(text):
    # Перечень заменяемых символов
    symbols = (' ', '.', ',', '!', '?', '-', '+', '*', '/', '<', '>', '—', '"', "'")
    for i in symbols:
        text = text.replace(i, '')
#    text = text.replace(' ', '')
#    text = text.replace('.', '')
#    text = text.replace(',', '')
#    text = text.replace('!', '')
#    text = text.replace('?', '')
#    text = text.replace('-', '')
#    text = text.replace('—', '')
#    text = text.replace('+', '')
#    text = text.replace('*', '')
#    text = text.replace('/', '')
#    text = text.replace('"', '')
#    text = text.replace("'", '')
    return text


# Функция ввода слова
def enter_word():
    return input('Enter palindrome or not:')


# Функция сравнения введенного слова с перевернутой копией
def check(word, word_revers):
    global string
    if word == word_revers:
        print(f'{string} - is a palindrome!')
    else:
        print(f'{string} - is not a palindrome!')


# Функция перевертывания слова
def revers(revers_word):
    word = ''
    i = len(revers_word)
    while i:
        word += revers_word[i-1]
        i -= 1
    return word


# Главная функция
def main():
    global string
    string = enter_word()
    string_revers = revers(string)
    check(replace_symbols(string.upper()), replace_symbols(string_revers.upper()))
#    check(string, string_revers)


# Начало программы
string = ''
if __name__ == '__main__':
    main()
