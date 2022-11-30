"""1. Напишите программу, которая 
- принимает на вход число N и 
- выдаёт следующую последовательность из N членов: 1, -3, 9, -27, 81, …

Ввод: значения типа <int>
Вывод: последовательность значений типа <int>
"""

N = int(input('Введите число N '))
for i in range(0, N):
    f = 3**i*(-1)**i
    print(f, end = '  ')


# # Вариант 2й группы
# n = int(input('Введите число N '))
# result = [1]
# for _ in range(n):
#     print(*result)
#     result.append(result[- 1] * (-3))
# print(*result)

# #Вариант Данила
# N = int(input('Введите число N '))
# output = -1 / 3
# print(*(output := int(output * -3) for i in range(N)), sep=', ') 