# Задача 1:
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# a = int(input('Введите целое число: '))
# b = ''
# while a > 0:
#     b = str(a % 2) + b
#     a = a // 2
# print(b)

# Задача 2:
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# def totalfibonacci (n):
#     if n == 0:
#         return 0
#     elif n in (1, 2):
#         return 1
#     elif n > 0:
#         return totalfibonacci(n - 1) + totalfibonacci(n - 2)
#     else:
#         return totalfibonacci(n + 2) - totalfibonacci(n + 1)  

# a = int(input('Введите целое число: ')) 

# l = []
# for i in range (-a, a+1):
#     l.append(totalfibonacci(i))
# print(l)    

# Задача 3:
# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# spisok = input("Введите несколько чисел разделив пробелом: ").split()
# for i in range(len(spisok)):
#     spisok[i] = int(spisok[i])
# print(spisok)
# min = spisok[0]
# max = spisok[1]
# for i in spisok:
#     if min > i:
#         min = i
#     if max < i:
#         max = i
# print (f"Min = {min}, Max = {max}")

# Задача 4. Задайте два целых числа. Напишите программу, 
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

def least_com_mult(a, b):
    if a > b:
        max, min = a, b
    else:
        max, min = b, a
    lcm = max
    while lcm%min != 0:
        lcm +=max
    return lcm

num1 = int(input("Введите первое число: ")) 
num2 = int(input("Введите второе число: "))

print("Наименьшее общее кратное чисел ", num1, " и ", num2, " равняется ", least_com_mult(num1, num2))