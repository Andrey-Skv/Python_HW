# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988

number = float(
    input('Введите число с любым количеством знаков после запятой : '))
correctness = int(input('Задайте точность числа : '))
print(f'{round(number, correctness):.{correctness}f}')
