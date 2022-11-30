""""3. Напишите программу, в которой 
- пользователь будет задавать две строки, а 
- программа - определять количество вхождений одной строки в другой.

Ввод: два значения типа <str>
Вывод: значение типа <int>

Пример:
hello world
hello
1
hello world
o
2
"""

str1 = input("Введите первую сторку: ")
str2 = input("Введите вторую сторку: ")

print(str1.count(str2))

# #Вариант Данила 
# str1 = input("Введите первую сторку: ")
# str2 = input("Введите вторую сторку: ")

# inkrement = 0
# for i in range(len(str1)):
#     if str2 in str1[i:]:
#         inkrement += 1
# print(inkrement)

# print(str1.count(str2))

# #Мое решение
# str_one = 'good news everyone, or one'
# str_two = 'one'
# #S.find(str, [start], [end])
# count = 0
# index = 0
# start = index
# while index != -1:
#     if str_one.find(str_two, start+1) != -1:
#         index = str_one.find(str_two, start+1)
#         start = index
#         count += 1
#     else:
#         index = -1
# print(count)
