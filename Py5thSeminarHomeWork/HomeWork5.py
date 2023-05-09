# Задача 26:  Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую степень B 
# с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def recr_degree(a, b):
#     if b == 0:
#         return 1
#     return a * recr_degree(a, b - 1)


# a = int(input('Print a num: '))
# b = int(input('Print degree for num: '))

# print(recr_degree(a, b))

# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def sumnum(a, b):
    if b == 0:
        return a    
    return sumnum (a, b - 1) + 1

a = int(input('Print 1st num: '))
b = int(input('Print second num: '))

print(sumnum(a, b))