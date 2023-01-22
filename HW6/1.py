# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]
import random as r
from random import randint

def greater_than_previous(nums):
    return [num for i, num in enumerate(nums) if i > 0 and num > nums[i-1]]
    
num = [randint(0,100) for _ in range(10)]
print((num))
print(greater_than_previous(num))