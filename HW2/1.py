# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

num = input('Введите число: ')
sum = 0
for i in num:
    if i.isdigit() == True:
        sum += int(i)
print(sum)