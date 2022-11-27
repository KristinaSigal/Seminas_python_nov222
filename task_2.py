# 2. Напишите программу, которая 
# - на вход принимает 5 чисел и 
# - находит максимальное из них.
# Ввод: любая коллекция значений типа <int>
# Вывод: значение типа <int>

a = int(input('Введите число a '))
b = int(input('Введите число b '))
c = int(input('Введите число c '))
d = int(input('Введите число d '))
e = int(input('Введите число e '))

some_list = [a, b, c, d, e]
print(some_list)
max = some_list[0]
for i in some_list:
    if max < i: 
        max = i
print(max)
