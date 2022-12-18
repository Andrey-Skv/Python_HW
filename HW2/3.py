# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6

# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

num_list = []
sum = 0
n = int(input("Введите число "))
for k in range(1,n+1):
    num_list.append((1+1/k)**k)
    sum +=(1+1/k)**k
    my_rounded_list = [round(k, 3) for k in num_list]
print(my_rounded_list)
print(round(sum, 3))