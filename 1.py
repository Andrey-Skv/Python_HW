# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.
# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# 1 `Версия

num = int(input("Введите день недели -"))
while num>7:
    num = int(input("Введите день недели -"))
if 1<=num<=5:
    print("Это будний день")
else: print("Выходной")

# 2 Версия

num = int(input("Введите день недели -"))
if 1<=num<=5:
    print("Это будний день")
elif num==6 or num==7:
    print("Выходной")
else: print("Это не день недели")