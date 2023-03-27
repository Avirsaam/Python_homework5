#
# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def my_power(number, pow):
    if pow == 0:
        return 1
    else:
        return number * my_power(number, pow - 1)

n = 2
p = 8
print(f'{n} в степени {p} равно {my_power(n, p)}')