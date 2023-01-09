# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8

from random import sample


def sum_elements(amount):
    new_list = sample(range(1, (amount+1)*3), k=amount)
    print(new_list)
    summ = 0
    for i in range(len(new_list)):
        if i % 2 == 0:
            summ += new_list[i]
    return summ


my_list = sum_elements(int(input("Enter amount - ")))
print(my_list)

# Второй способ

some_list = [int(input('введите элемент списка: '))
             for _ in range(int(input('Введите кол-во элементов: ')))]
print(f'Сумма элементов {[some_list[i] for i in range(len(some_list)) if i%2 == 0]} ,\
 стоящих на нечетных позициях = {sum([some_list[i] for i in range(len(some_list)) if i%2 == 0])}')

