# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def recursive_sum(a, b):
    if b == 0:
        return a
    else:
        return recursive_sum(a, b - 1) + 1

number_1 = 66
number_2 = 11
print(f'{number_1} + {number_2} = {recursive_sum(number_1, number_2)}')