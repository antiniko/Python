# Задача 33:
# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k. 
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите натуральную степень k: '))
f = open("HW_1.txt", "w") # 

for i in range(k):
    a = randint(0, 100) 
    if a !=0:
        f.write(f"{a}*x^{k-i} + ") 
    print (a, end=" ") 
a = randint(0, 100) 
if a !=0:
    f.write(f"{a}") 
f.write(f" = 0") 
f.close() 

# Задача 35:
# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

# import os
# import sys 

# f = open(os.path.join(sys.path[0],"HW.txt"), "r") 
# buf = f.read()
# input = buf.split()
# input = list(map(lambda x: int(x), input)) 
# print(input)
# for i in range(1,len(input)):
#     if input[i-1] != input[i] - 1: 
#         print(f"Пропущено {input[i-1]+1}") 


# Задача 43:
# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# numbers = [1, 2, 3, 5, 1, 5, 3, 10]

# def get_unique_num(numbers):
#     unique = []

#     for i in numbers:
#         count = 0
#         for j in numbers:
#             if i == j:
#                 count+=1
#         if count == 1:
#             unique.append(i)
#     return unique

# print(get_unique_num(numbers))