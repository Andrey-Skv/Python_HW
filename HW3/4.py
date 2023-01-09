#  4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

some_list = [float(input('Введите элемент списка - '))
             for _ in range(int(input('Введите количество элементов - ')))]
new_list = []
for i in range(len(some_list)-1):
    if some_list[i] - int(some_list[i]) == 0:
        some_list.remove(some_list[i])
for i in range(len(some_list)):
    new_list.append(round((some_list[i] % 1), 3))
    # difference=round((max(new_list)-min(new_list)),3)
print(f'{new_list} => {round((max(new_list)-min(new_list)),3)}')
