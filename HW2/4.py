# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

n = int(input('Введите количество элементов :   '))
run = range(-n, n+1)
numbers = list(run)
print(numbers)
result = 1
for i in numbers:
    print(i)
    s = input('Укажите позицию для вычисления - ')
    d = input('Укажите позицию для вычисления - ')
    result = (s)*(d)
print(f'Произведение чисел под заданными номерами  = {result}')
