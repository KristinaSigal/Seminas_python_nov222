# 2. Напишите программу, которая 
# - на вход принимает 5 чисел и 
# - находит максимальное из них.
# Ввод: любая коллекция значений типа <int>
# Вывод: значение типа <int>

some_list = []
for i in 1, 2, 3, 4, 5:
    some_list.append(int(input(f'введите {i} значение: ')))
print (some_list)
max = some_list[0]
for i in some_list:
    if max < i:
        max=i
print(f'максимальное число {max}')
