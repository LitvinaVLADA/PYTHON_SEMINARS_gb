# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def SUM(A, B):
    if B == 0:
        return A
    return SUM(A, B-1) + 1

A = int(input('Введите первое число: '))
B = int(input('Введите второе число: '))

result = SUM (A,B)

print(A, '+', B, '=', result)