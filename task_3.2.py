'''2. Задайте список целых чисел. Найти количество пар элементов, равных друг другу.

Ввод: значения типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <int>

Примеры:
[3, 3, 4, 7] -> 1
[4, 4, 4] -> 3	
[3, 3, 3, 3, 3] -> 10
'''

# list_1 = [3, 3, 4, 7]
# list_2 = [4, 4, 4]
# list_3 = [3, 3, 3, 3, 3]

# my_list = list_1
# res = 0

# for i in range(len(my_list)):
#     for j in range(i + 1, len(my_list)):
#         if my_list[i] == my_list[j]:
#             res += 1
# print(res)

# # Вариант2

# size = int(input('Введите размерность: '))
# import random
# a = 0
# new_list = [random.randint(1, 9) for i in range(size)]
# print(new_list)
# for l in range(size):
#     for k in new_list[l + 1:]:
#         if new_list[l] == k:
#             a += 1
# print(a)

# Вар Данила

lst = [3, 3, 4, 7]
# lst = [4, 4, 4]
# lst = [3, 3, 3, 3, 3]

pairs = 0
for i, el in enumerate(lst): # (index, element)
    pairs += lst[i + 1:].count(el)

print(pairs)
