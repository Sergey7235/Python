# print('Как тебя зовут?\n')
# name = input()
# print('Рад познакомиться, ', name, '!', sep='')
# age = 0
# while age != 777:
#     age = int(input('Сколько тебе лет, ' + name + '?\n'))

# a = [1, 21, 31, 41, 51, 61, 71, 81, 91]
# b = set([range(2, 4), range(32, 34), range(42, 44), range(52, 54), range(62, 64), range(72, 74), range(82, 84),
#      range(92, 94)])
# print(type(b))
# x = range(2, 4)
# # x = 3
# if x in b:
#     print(a)
#
# if age == 1:
#     print()
# x = age + 1

# if (x >= 5) and (x <= 20):
#     print('А я думал, тебе', x, 'лет!')
# elif (x <= 4) and (x >= 2) and (x >= 22) and (x <= 24):
#     print('А я думал, тебе', x, 'года!')
# elif (x % 10 == 1):
#     print('А я думал, тебе', x, 'год!')
# elif x % 10 == 1:
# print('А я думал, тебе', x, 'год!')

# PEP8
# from typing import Dict
#
# d: Dict[str, int] = {'Moscow': 1, 'St_Petersburg': 2}
# print(type(d))
# for key in d:
#     print(key, d[key], sep=" - ")


# ctrl + c ctrl + w - нету мыслей в голове
# D - don't
# R - repeat
# Y - yourself
#
# W - we
# E - enjoy
# T - typing


def is_year_leap(x):
    if ((x % 4) == 0) and ((x % 100) != 0):
        print("Год високосный!")
    elif (x % 400) != 0:
        print("Год не високосный!")


flag = "true"
while flag == "true":
    x = int(input("Введите год: "))
    if x == 777:
        flag = "false";
    is_year_leap(x)
