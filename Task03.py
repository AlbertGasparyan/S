# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

check = False
while not check:
    x = int(input("x: "))
    y = int(input("y: "))
    if (x != 0 or y != 0):
        check = True
    else:
        print('Х и У должны быть больше или меньше 0!\n Попробуйте еще раз!')

if x > 0 and y > 0:
    print('1 четверть')
elif x < 0 and y > 0:
    print('2 четверть')
elif x < 0 and y < 0:
    print('3 четверть')
elif x > 0  and y < 0:
    print('4 четверть')
elif x == 0:
    print('Точка на оси x')
else:
    print('Точка на оси y')