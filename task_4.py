# 4. Напишите программу, которая будет 
# - принимать на вход дробь и 
# - показывать первую цифру дробной части числа.
# Ввод: значение типа <float>
# Вывод: значение типа <int>

# Примеры:
# 6.78 -> 7
# 5 -> 0
# 0,34 -> 3

num = float(input('Введите число '))
print(int(num * 10 % 10))

# num = input('Введите число ').split('.')
# print(num[-1][0])