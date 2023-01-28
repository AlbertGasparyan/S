# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math

# x1=float(input('Введите значение x1:'))
# y1=float(input('Введите значение y1:'))
# x2=float(input('Введите значение x2:'))
# y2=float(input('Введите значение y2:'))

x1, y1 = [int(s) for s in input("Input x1 and y1: ").split(',')]
x2, y2 = [int(s) for s in input("Input x2 and y2: ").split(',')]


distance = math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2))
print(distance)