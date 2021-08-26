print('Проход по диапазону чисел от 0 до 100,')
print('вывод всех чисел, при этом пропустить число 4 и выход из цикла на 18')
# 1 - for
print('For:')
for i in range(0,100):
    if i == 4:
        continue
    elif i == 18:
        break
    print(i)
# 2 - while
print('While:')
i = 0
while i <= 100:
    if i == 4:
        i += 1
        continue
    elif i == 18:
        break
    print(i)
    i += 1