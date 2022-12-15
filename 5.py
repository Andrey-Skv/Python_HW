# 5. Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
#  https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1

print("Ввведите координаты точки A")
xa = int(input('X1 = '))
ya = int(input("Y1 = "))

print("Ввведите координаты точки B")
xb = int(input('X2 = '))
yb = int(input("Y2 = "))

AB = round(((xb-xa)**2 + (yb-ya)**2)**(1/2), 3)
print(
    f'Расстояние между точками координатами ({xa}, {ya}); ({xb}, {yb}) = {AB}')
