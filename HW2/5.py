# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random


def mix(mix_list):
    mix_list(:) = my_list
    for i in range(len(mix_list)):
        # Получение случайного индекса
        index_aleatory = random.randint(0, len(mix_list) - 1)
        # Замена
        temp = mix_list[i]
        mix_list[i] = mix_list[index_aleatory]
        mix_list[index_aleatory] = temp
        # Возвращаем список
        return mix_list
my_list = [1,2,3,4,5]
shuf_list= mix(my_list)
print(my_list)
print(shuf_list)
    
# import random
# def mix_list(list_original):
#     # Создаем копию, поскольку мы не должны изменять оригинал
#     list = list_original[:]
#     # Цикл от 0 до длины списка -1
  
#     for i in range(len(list)):
#         # Получение случайного индекса
#         index_aleatory = random.randint(0, len(list) - 1)
#         # Замена
#         temp = list[i]
#         list[i] = list[index_aleatory]
#         list[index_aleatory] = temp
#     # Возвращаем список
#     return list
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# mixed_list = mix_list(list)
# print("Исходный список: ")
# print(list)
# print("Перемешанный список: ")
# print(mixed_list)