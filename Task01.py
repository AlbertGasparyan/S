# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет


enter_user = int(input("Введите пожалуйста цифру соответствующую дню недели:"))

def NumDays(num):
    if 1<num<6:
        print('День ялвяется будним!')
    if num==6 or num==7:
        print('День ялвяется выходным!')
    if num<0 or num>7:
        print('Вы ввели неверное число!')
    if num == 0:
        print('Вы ввели неверное число!')

NumDays(enter_user)