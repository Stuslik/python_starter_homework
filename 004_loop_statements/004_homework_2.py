print('В предложении “Hello world” заменить все буквы “o” на “a” , а буквы “l”  на “e”')
string = 'Hello world'
# Нужно получить = 'Heeea wared'
# 1 - for
print('For:')
res = ''
for i in string:
    if i == 'o':
        res += 'a'
    elif i == 'l':
        res += 'e'
    else:
        res += i
print(res)
# 1 - while
print('While:')
res = ''
i = 0
while i < len(string):
    if string[i] == 'o':
        res += 'a'
    elif string[i] == 'l':
        res += 'e'
    else:
        res += string[i]
    i += 1
print(res)