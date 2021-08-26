import math
print("Вычисление функции y = f(x)")
x = float(input("Введите значение х: "))
if -math.pi <= x and x <= math.pi:
    y = round(math.cos(3 * x),2)
elif x < -math.pi or x > math.pi:
    y = x
print("y = x = " + str(y) if y == x else "y = cos(3x) = " + str(y))