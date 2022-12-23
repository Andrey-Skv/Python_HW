# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def antifib(n):
    if n >= 0:
        return 1
    else:
        return antifib(n+2) - antifib(n+1)


number = int(input('Введите число : '))
list1 = [fib(i) for i in range(0, number)]
list2 = [antifib(i) for i in range(-1, -number - 2, -1)]
list2.reverse()
list2.extend(list1)
print(list2)

