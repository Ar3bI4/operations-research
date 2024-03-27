# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# import copy
# e = 0.00001
# a = int(input("0 - Минимум  1 - Максимум"))
# func_coef = [3, 2]  # коэфы в функционале
# lim_coef_st = [  # коэфы в ограничениях (потом преобразуется в lim_coef1)
#     [2, 1, 1, 0],
#     [1, 4, 0, 1],
# ]
# lim_coef = []
# right_part = [6, 5]  # вектор В
# Z = []  # самая нижняя сторочка
# resh_Str = 0
# resh_Stol = 0
# resh_Coef = 10000000
# resh_Elem = 0
# max_Z = 0
# min_Z = 0
# flag = 1
# numberR = []
#
# print(numberR)
#
# for j in range(len(func_coef)):
#     Z.append((-1) * func_coef[j])
# for j in range(len(lim_coef_st)):
#     Z.append(0)
#     Z.append(0)
#
# if (a == 0):
#     M = 10000
# if (a == 1):
#     M = -10000
#
# # добавленине х' и x''(разделение  одной переменной на две)
# for i in range(len(lim_coef_st)):
#     if (right_part[i] < 0):
#         for k in range(len(lim_coef_st[i])):
#             lim_coef_st[i][k] = lim_coef_st[i][k] * (-1)
#         right_part[i] = right_part[i] * (-1)
#     lim_coef.append([])
#     for j in range(len(lim_coef_st[i])):
#         lim_coef[i].append(lim_coef_st[i][j])
#
# # # вывод для проверки
# # for j in range(len(lim_coef)):
# #     print(lim_coef[j])
# # print(Z)
# # print(' ')
# #
# # # вывод для проверки
# # for j in range(len(lim_coef)):
# #     print(lim_coef[j])
# # print(Z)
# # print(' ')
#
# # добавление 1 и 0 для R
# for i in range(len(lim_coef)):
#     for j in range(len(lim_coef)):
#         if (i == j):
#             lim_coef[i].append(1)
#         else:
#             lim_coef[i].append(0)
#
# print(' ')
# summ = 0
#
# for i in range(len(lim_coef[0]) - len(lim_coef)):
#     for j in range(len(lim_coef)):
#         summ = summ + lim_coef[j][i]
#     Z[i] = Z[i] + summ * M
#     summ = 0
#
# srp = 0
# for i in range(len(right_part)):
#     srp = srp + right_part[i]
# Z.append(M * srp)
#
# # вывод для проверки
# # for j in range(len(lim_coef)):
# #     print(lim_coef[j])
# # print(Z)
# # print(' ')
#
# # решающий столбец
# for i in range(len(Z) - 1):
#     if (a == 0):
#         if (Z[i] > 0) and (abs(Z[i]) > abs(max_Z)):
#             max_Z = Z[i]
#             resh_Stol = i
#     if (a == 1):
#         if (Z[i] < 0) and (abs(Z[i]) > abs(max_Z)):
#             max_Z = Z[i]
#             resh_Stol = i
#
# print(resh_Stol)
#
# max_Z = 0
# err_full_skip = 0
# # оптимальный план
# opt_pl = []
# for i in range(len(Z) - 1):
#     opt_pl.append(0)
#
# # решающя строка
# for i in range(len(right_part)):
#     if lim_coef[i][resh_Stol] <= 0:
#         err_full_skip = err_full_skip + 1
#         continue
#     if right_part[i] == 0:
#         err_full_skip = err_full_skip + 1
#         continue
#     if (right_part[i] / lim_coef[i][resh_Stol] < resh_Coef):#выбор решающей строки
#         resh_Coef = right_part[i] / lim_coef[i][resh_Stol]
#         resh_Str = i
# if (err_full_skip == len(right_part)): raise SystemExit("Невозможно найти оптимальный план")
# err_full_skip = 0
#
# # print(resh_Stol)
# # print('')
#
# resh_Coef = 10000000
#
# resh_Elem = lim_coef[resh_Str][resh_Stol]
#
# # копирование матрицы коэффициентов
# lim_coef_prev = []
# lim_coef_cur = []
# for i in range(len(lim_coef)):
#     lim_coef[i].append(right_part[i])
# lim_coef.append(Z)
#
# lim_coef_prev = copy.deepcopy(lim_coef)
# lim_coef_cur = copy.deepcopy(lim_coef)
#
# temp = 0
#
# # вывод для проверки
# # for j in range(len(lim_coef)):
# #     print(lim_coef[j])
# # print(resh_Str)
# # print(resh_Stol)
#
# # Максимум
# if (a == 1):
#     while (flag != 0):
#         flag = 0
#         if (temp != 0):
#             # решающий столбец
#             for i in range(len(Z) - 1):
#                 if (Z[i] < 0) and (abs(Z[i]) > abs(max_Z)):
#                     max_Z = Z[i]
#                     resh_Stol = i
#             max_Z = 0
#
#             # решающя строка
#             for i in range(len(right_part)):
#                 if lim_coef_prev[i][resh_Stol] <= 0:
#                     err_full_skip = err_full_skip + 1
#                     continue
#                 if right_part[i] == 0:
#                     err_full_skip = err_full_skip + 1
#                     continue
#                 if (right_part[i] / lim_coef_prev[i][resh_Stol] < resh_Coef):
#                     resh_Coef = right_part[i] / lim_coef_prev[i][resh_Stol]
#                     resh_Str = i
#             resh_Coef = 10000000
#             if (err_full_skip == len(right_part)): raise SystemExit("Невозможно найти оптимальный план строка")
#             err_full_skip = 0
#
#         # print(resh_Str)
#         # print(resh_Stol)
#         resh_Elem = lim_coef_prev[resh_Str][resh_Stol]
#
#         # деление решающей строки на решающий элемент
#         for i in range(len(lim_coef[1])):
#             lim_coef_cur[resh_Str][i] = lim_coef_cur[resh_Str][i] / resh_Elem
#
#         # зануление решающего столбца
#         for i in range(len(right_part) + 1):
#             if (i != resh_Str):
#                 lim_coef_cur[i][resh_Stol] = 0
#
#         # метод прямоугольника
#         for i in range(len(lim_coef_prev)):
#             if (i == resh_Str): continue
#             for j in range(len(lim_coef_prev[i])):
#                 if (j == resh_Stol): continue
#                 lim_coef_cur[i][j] = lim_coef_prev[i][j] - lim_coef_prev[resh_Str][j] * lim_coef_prev[i][resh_Stol] / \
#                                      lim_coef_prev[resh_Str][resh_Stol]
#
#         Z = copy.deepcopy(lim_coef_cur[len(lim_coef_cur) - 1])
#         for i in range(len(lim_coef_cur) - 1):
#             right_part[i] = lim_coef_cur[i][len(lim_coef_cur[i]) - 1]
#
#         # проверка
#         for i in range(len(lim_coef_cur[len(lim_coef_prev) - 1]) - 1):
#             if (lim_coef_cur[len(lim_coef_cur) - 1][i] < 0):
#                 flag = 1
#
#         lim_coef_prev = copy.deepcopy(lim_coef_cur)
#
#         temp = temp + 1
#         # вывод для проверки
#     #     for j in range(len(lim_coef_cur)):
#     #         print(lim_coef_cur[j])
#     # print("")
#     # print("")
#
# # Минимум
# if (a == 0):
#     while (flag != 0):
#         flag = 0
#         if (temp != 0):
#             # решающий столбец
#             for i in range(len(Z) - 1):
#                 if (Z[i] > 0) and (abs(Z[i]) > abs(max_Z)):
#                     max_Z = Z[i]
#                     resh_Stol = i
#             max_Z = 0
#
#             # решающя строка
#             for i in range(len(right_part)):
#                 if lim_coef_prev[i][resh_Stol] <= 0:
#                     err_full_skip = err_full_skip + 1
#                     continue
#                 if right_part[i] == 0:
#                     err_full_skip = err_full_skip + 1
#                     continue
#                 if (right_part[i] / lim_coef_prev[i][resh_Stol] < resh_Coef):
#                     resh_Coef = right_part[i] / lim_coef_prev[i][resh_Stol]
#                     resh_Str = i
#             if (err_full_skip == len(right_part)): raise SystemExit("Невозможно найти оптимальный план строка")
#             err_full_skip = 0
#             resh_Coef = 10000000
#
#         resh_Elem = lim_coef_prev[resh_Str][resh_Stol]
#         # деление решающей строки на решающий элемент
#         for i in range(len(lim_coef[1])):
#             lim_coef_cur[resh_Str][i] = lim_coef_cur[resh_Str][i] / resh_Elem
#
#         # зануление решающего столбца
#         for i in range(len(right_part) + 1):
#             if (i != resh_Str):
#                 lim_coef_cur[i][resh_Stol] = 0
#
#         # метод прямоугольника
#         for i in range(len(lim_coef_prev)):
#             if (i == resh_Str): continue
#             for j in range(len(lim_coef_prev[i])):
#                 if (j == resh_Stol): continue
#                 lim_coef_cur[i][j] = lim_coef_prev[i][j] - lim_coef_prev[resh_Str][j] * lim_coef_prev[i][resh_Stol] / \
#                                      lim_coef_prev[resh_Str][resh_Stol]
#
#         Z = copy.deepcopy(lim_coef_cur[len(lim_coef_cur) - 1])
#         for i in range(len(lim_coef_cur) - 1):
#             right_part[i] = lim_coef_cur[i][len(lim_coef_cur[i]) - 1]
#
#         # проверка
#         for i in range(len(lim_coef_cur[len(lim_coef_prev) - 1]) - 1):
#             if (lim_coef_cur[len(lim_coef_cur) - 1][i] > 0):
#                 flag = 1
#
#         lim_coef_prev = copy.deepcopy(lim_coef_cur)
#
#         temp = temp + 1
#
#         # вывод для проверки
#     #     for j in range(len(lim_coef_cur)):
#     #         print(lim_coef_cur[j])
#     #     print(resh_Str)
#     #     print(resh_Stol)
#     # print("")
#     # print("")
#
# for i in range(len(right_part)):
#     for j in range(len(lim_coef_cur[i]) - 1):
#         if (lim_coef_cur[i][j] == 1):
#             opt_pl[j] = right_part[i]
#
# for i in range(len(right_part)):
#     opt_pl.pop(len(opt_pl) - 1)
#
# check = 0
# for i in range(len(opt_pl) - len(right_part), len(opt_pl)):
#     if (opt_pl[i] > 0):
#         check += 1
#
# print("Оптимальный план:", opt_pl)
# print("Оптимум:", lim_coef_cur[len(lim_coef_cur) - 1][len(lim_coef_cur[len(lim_coef_cur) - 1]) - 1])
# print('')
# print('')
# print('')
# print('')
#
# chekerer = 0
# while(1):
#     if chekerer == 0:
#         #пошёл Гомори
#         lim_coef_st = copy.deepcopy(lim_coef_cur)
#         print('lim_coef копия')
#
#         for i in range(len(lim_coef_st)):
#             for j in range(len(lim_coef_st)-1):
#                 lim_coef_st[i].pop(len(lim_coef_st[i])-2)#удаление ограничений
#
#         for i in range(len(lim_coef_st)):
#             print(lim_coef_st[i])
#         print('')
#
#     NotInt = []
#     numNotInt = []
#     for i in range(len(lim_coef_st)-1):
#         NotInt.append(lim_coef_st[i][len(lim_coef_st[i])-1])#добавление нового столбца
#
#     print(NotInt)
#     print('\n')
#
#     for i in range(len(NotInt)):
#         if abs(round(NotInt[i])-NotInt[i]) > e:#проверка числа на целость
#             numNotInt.append(i)
#
#     if (numNotInt == []):
#         print("Оптимальный план:", round(-1*lim_coef_st[-1][-1]))
#         break
#
#     print(numNotInt)
#     print('\n')
#
#     maxDrob = -1
#     maxDrobNum = -1
#
#     for i in numNotInt:
#         if NotInt[i] % 1 > maxDrob:#поиск наибольшей дробной части
#             maxDrob = NotInt[i] % 1
#             maxDrobNum = i
#     print(maxDrobNum)
#     print('')
#
#     newStr = []
#     for i in range(len(lim_coef_st[maxDrobNum])):
#         newStr.append((lim_coef_st[maxDrobNum][i] % 1)*(-1))#добавление ограничения
#
#     newStr.append(1)#базисная единица
#     newStr[-1],newStr[-2] = newStr[-2],newStr[-1]
#     print(newStr)
#     print('')
#
#     for i in range(len(lim_coef_st)):
#         lim_coef_st[i].append(0)
#         lim_coef_st[i][-1], lim_coef_st[i][-2] = lim_coef_st[i][-2], lim_coef_st[i][-1]#меняем последний и предпоследний столбцы местами
#     lim_coef_st.append(newStr)
#     lim_coef_st[-1], lim_coef_st[-2] = lim_coef_st[-2], lim_coef_st[-1]#меняем последнюю и предпоследнюю строки местами
#     if (chekerer == 0):
#         for i in range(len(lim_coef_st[-1])):
#             lim_coef_st[-1][i] *= -1#домножение индексной строки на -1
#     for i in range(len(lim_coef_st)):
#         print(lim_coef_st[i])
#     print('')
#
#     #Переделанный симплекс
#
#     flag = 1
#
#     resh_Coef = 10000000
#
#     #решающая строка
#     resh_Str = len(lim_coef_st) - 2
#     print(resh_Str)
#     # решающий столбец
#     for i in range(len(lim_coef_st[-1])):
#         if lim_coef_st[-2][i] == 0:
#             continue
#         if lim_coef_st[-1][i] == 0:
#             continue
#         if (lim_coef_st[-1][i] / lim_coef_st[-2][i] < resh_Coef):
#             resh_Coef = lim_coef_st[-1][i] / lim_coef_st[-2][i]
#             resh_Stol = i
#
#     print(resh_Stol)
#     print('')
#
#
#     resh_Coef = 10000000
#
#
#     resh_Elem = lim_coef_st[resh_Str][resh_Stol]
#     print(resh_Elem)
#
#     # копирование матрицы коэффициентов
#     lim_coef_prev = copy.deepcopy(lim_coef_st)
#
#     #деление строки на решающий элемент
#     for i in range(len(lim_coef_st[-2])):
#         lim_coef_st[-2][i] = lim_coef_prev[-2][i] / resh_Elem
#
#     # зануление решающего столбца
#         for i in range(len(lim_coef_st)):
#             if (i != resh_Str):
#                 lim_coef_st[i][resh_Stol] = 0.0
#
#     # метод прямоугольника
#         for i in range(len(lim_coef_prev)):
#             if (i == resh_Str): continue
#             for j in range(len(lim_coef_prev[i])):
#                 if (j == resh_Stol): continue
#                 lim_coef_st[i][j] = lim_coef_prev[i][j] - lim_coef_prev[resh_Str][j] * lim_coef_prev[i][resh_Stol] / lim_coef_prev[resh_Str][resh_Stol]
#
#     #пересчитаная таблица
#     for i in range(len(lim_coef_st)):
#         print(lim_coef_st[i])
#     print('')
#     chekerer += 1


import copy
e = 0.0000001
a = int(input("0 - Минимум  1 - Максимум"))
func_coef = [2, -5, 2, -1, -1]  # коэфы в функционале
lim_coef_st = [  # коэфы в ограничениях (потом преобразуется в lim_coef1)
    [1, -14, 2, -1, -1],
    [10, -6, 9, -5, -2],
    [1, 3, 19, -10, -5]
]
lim_coef = []
right_part = [9, 2, 4]  # вектор В
Z = []  # самая нижняя сторочка
resh_Str = 0
resh_Stol = 0
resh_Coef = 10000000
resh_Elem = 0
max_Z = 0
min_Z = 0
flag = 1
numberR = []

print(numberR)

for j in range(len(func_coef)):
    Z.append((-1) * func_coef[j])
for j in range(len(lim_coef_st)):
    Z.append(0)


if (a == 0):
    M = 10000
if (a == 1):
    M = -10000

# приведение к каноническому
for i in range(len(lim_coef_st)):
    if (right_part[i] < 0):
        for k in range(len(lim_coef_st[i])):
            lim_coef_st[i][k] = lim_coef_st[i][k] * (-1)
        right_part[i] = right_part[i] * (-1)
    lim_coef.append([])
    for j in range(len(lim_coef_st[i])):
        lim_coef[i].append(lim_coef_st[i][j])

# # вывод для проверки
# for j in range(len(lim_coef)):
#     print(lim_coef[j])
# print(Z)
# print(' ')
#
# # вывод для проверки
# for j in range(len(lim_coef)):
#     print(lim_coef[j])
# print(Z)
# print(' ')

# добавление 1 и 0 для R
for i in range(len(lim_coef)):
    for j in range(len(lim_coef)):
        if (i == j):
            lim_coef[i].append(1)#новый базис
        else:
            lim_coef[i].append(0)

print(' ')
summ = 0

for i in range(len(lim_coef[0]) - len(lim_coef)):
    for j in range(len(lim_coef)):
        summ = summ + lim_coef[j][i]
    Z[i] = Z[i] + summ * M
    summ = 0

srp = 0
for i in range(len(right_part)):
    srp = srp + right_part[i]
Z.append(M * srp)

# вывод для проверки
# for j in range(len(lim_coef)):
#     print(lim_coef[j])
# print(Z)
# print(' ')

# решающий столбец
for i in range(len(Z) - 1):
    if (a == 0):
        if (Z[i] > 0) and (abs(Z[i]) > abs(max_Z)):
            max_Z = Z[i]
            resh_Stol = i
    if (a == 1):
        if (Z[i] < 0) and (abs(Z[i]) > abs(max_Z)):
            max_Z = Z[i]
            resh_Stol = i

print(resh_Stol)

max_Z = 0
err_full_skip = 0
# оптимальный план
opt_pl = []
for i in range(len(Z) - 1):
    opt_pl.append(0)

# решающая строка
for i in range(len(right_part)):
    if lim_coef[i][resh_Stol] <= 0:
        err_full_skip = err_full_skip + 1
        continue
    if right_part[i] == 0:
        err_full_skip = err_full_skip + 1
        continue
    if (right_part[i] / lim_coef[i][resh_Stol] < resh_Coef):
        resh_Coef = right_part[i] / lim_coef[i][resh_Stol]
        resh_Str = i
if (err_full_skip == len(right_part)): raise SystemExit("Невозможно найти оптимальный план")
err_full_skip = 0

# print(resh_Stol)
# print('')

resh_Coef = 10000000

resh_Elem = lim_coef[resh_Str][resh_Stol]

# копирование матрицы коэффициентов

lim_coef_prev = []
lim_coef_cur = []
for i in range(len(lim_coef)):
    lim_coef[i].append(right_part[i])
lim_coef.append(Z)

lim_coef_prev = copy.deepcopy(lim_coef)
lim_coef_cur = copy.deepcopy(lim_coef)

temp = 0

#вывод для проверки
for j in range(len(lim_coef)):
    print(lim_coef[j])
print(resh_Str)
print(resh_Stol)

# Максимум
if (a == 1):
    while (flag != 0):
        flag = 0
        if (temp != 0):
            # решающий столбец
            for i in range(len(Z) - 1):
                if (Z[i] < 0) and (abs(Z[i]) > abs(max_Z)):
                    max_Z = Z[i]
                    resh_Stol = i
            max_Z = 0
# решающя строка
            for i in range(len(right_part)):
                if lim_coef_prev[i][resh_Stol] <= 0:
                    err_full_skip = err_full_skip + 1
                    continue
                if right_part[i] == 0:
                    err_full_skip = err_full_skip + 1
                    continue
                if (right_part[i] / lim_coef_prev[i][resh_Stol] < resh_Coef):
                    resh_Coef = right_part[i] / lim_coef_prev[i][resh_Stol]
                    resh_Str = i
            resh_Coef = 10000000
            if (err_full_skip == len(right_part)): raise SystemExit("Невозможно найти оптимальный план строка")
            err_full_skip = 0

        # print(resh_Str)
        # print(resh_Stol)
        resh_Elem = lim_coef_prev[resh_Str][resh_Stol]

        # деление решающей строки на решающий элемент
        for i in range(len(lim_coef[1])):
            lim_coef_cur[resh_Str][i] = lim_coef_cur[resh_Str][i] / resh_Elem

        # зануление решающего столбца
        for i in range(len(right_part) + 1):
            if (i != resh_Str):
                lim_coef_cur[i][resh_Stol] = 0

        # метод прямоугольника
        for i in range(len(lim_coef_prev)):
            if (i == resh_Str): continue
            for j in range(len(lim_coef_prev[i])):
                if (j == resh_Stol): continue
                lim_coef_cur[i][j] = lim_coef_prev[i][j] - lim_coef_prev[resh_Str][j] * lim_coef_prev[i][resh_Stol] / \
                                     lim_coef_prev[resh_Str][resh_Stol]

        Z = copy.deepcopy(lim_coef_cur[len(lim_coef_cur) - 1])
        for i in range(len(lim_coef_cur) - 1):
            right_part[i] = lim_coef_cur[i][len(lim_coef_cur[i]) - 1]

        # проверка
        for i in range(len(lim_coef_cur[len(lim_coef_prev) - 1]) - 1):
            if (lim_coef_cur[len(lim_coef_cur) - 1][i] < 0):
                flag = 1

        lim_coef_prev = copy.deepcopy(lim_coef_cur)

        temp = temp + 1
        # вывод для проверки
    #     for j in range(len(lim_coef_cur)):
    #         print(lim_coef_cur[j])
    # print("")
    # print("")

# Минимум
if (a == 0):
    while (flag != 0):
        flag = 0
        if (temp != 0):
            # решающий столбец
            for i in range(len(Z) - 1):
                if (Z[i] > 0) and (abs(Z[i]) > abs(max_Z)):
                    max_Z = Z[i]
                    resh_Stol = i
            max_Z = 0

            # решающая строка
            for i in range(len(right_part)):
                if lim_coef_prev[i][resh_Stol] <= 0:
                    #err_full_skip = err_full_skip + 1
                    continue
                if right_part[i] == 0:
                    #err_full_skip = err_full_skip + 1
                    continue
                if (right_part[i] / lim_coef_prev[i][resh_Stol] < resh_Coef):
                    resh_Coef = right_part[i] / lim_coef_prev[i][resh_Stol]
                    resh_Str = i
            if (err_full_skip == len(right_part)): raise SystemExit("Невозможно найти оптимальный план строка")
            err_full_skip = 0
            resh_Coef = 10000000

        resh_Elem = lim_coef_prev[resh_Str][resh_Stol]
        # деление решающей строки на решающий элемент
        for i in range(len(lim_coef[1])):
            lim_coef_cur[resh_Str][i] = lim_coef_cur[resh_Str][i] / resh_Elem

        # зануление решающего столбца
        for i in range(len(right_part) + 1):
            if (i != resh_Str):
                lim_coef_cur[i][resh_Stol] = 0

        # метод прямоугольника
        for i in range(len(lim_coef_prev)):
            if (i == resh_Str): continue
            for j in range(len(lim_coef_prev[i])):
                if (j == resh_Stol): continue
                lim_coef_cur[i][j] = lim_coef_prev[i][j] - lim_coef_prev[resh_Str][j] * lim_coef_prev[i][resh_Stol] / \
                                     lim_coef_prev[resh_Str][resh_Stol]
        Z = copy.deepcopy(lim_coef_cur[len(lim_coef_cur) - 1])
        for i in range(len(lim_coef_cur) - 1):
            right_part[i] = lim_coef_cur[i][len(lim_coef_cur[i]) - 1]

        # проверка
        for i in range(len(lim_coef_cur[len(lim_coef_prev) - 1]) - 1):
            if (lim_coef_cur[len(lim_coef_cur) - 1][i] > 0):
                flag = 1

        lim_coef_prev = copy.deepcopy(lim_coef_cur)

        temp = temp + 1

        # вывод для проверки
        for j in range(len(lim_coef_cur)):
            print(lim_coef_cur[j])
    print(resh_Str)
    print(resh_Stol)
print("")
print("")

for i in range(len(right_part)):
    for j in range(len(lim_coef_cur[i]) - 1):
        if (lim_coef_cur[i][j] == 1):
            opt_pl[j] = right_part[i]

for i in range(len(right_part)):
    opt_pl.pop(len(opt_pl) - 1)

check = 0
for i in range(len(opt_pl) - len(right_part), len(opt_pl)):
    if (opt_pl[i] > 0):
        check += 1

print("Оптимальный план:", opt_pl)
print("Оптимум:", lim_coef_cur[-1][-1])
print('')
print('')
print('')
print('')

chekerer = 0
while(1):
    if chekerer == 0:
        #Начало Гомори
        lim_coef_st = copy.deepcopy(lim_coef_cur)
        print('lim_coef копия')

        for i in range(len(lim_coef_st)):
            for j in range(len(lim_coef_st)-1):
                lim_coef_st[i].pop(len(lim_coef_st[i])-2)

        for i in range(len(lim_coef_st)):
            print(lim_coef_st[i])
        print('')

    NotInt = []
    numNotInt = []
    for i in range(len(lim_coef_st)-1):
        NotInt.append(lim_coef_st[i][len(lim_coef_st[i])-1])

    print(NotInt)
    print('\n')

    for i in range(len(NotInt)):
        if abs(round(NotInt[i])-NotInt[i]) > e:
            numNotInt.append(i)

    if (numNotInt == []):
        base =[]
        numR = -1
        isOne = 0
        numZero = 0

        for i in range(len(lim_coef_st)):
            for j in range(len(lim_coef_st)):
                if lim_coef_st[j][i] == 1:
                    isOne = 1
                    numR = j
                if abs(lim_coef_st[j][i]) < e: numZero += 1
            if (isOne == 1) and (numZero >= len(lim_coef_st)-2):
                base.append(numR)
            else: base.append(-1)
            numR = -1
            isOne = 0
            numZero = 0
        print(base)

        res = []
        for i in base:
            if i != -1:  res.append(round(lim_coef_st[i][-1]))
            else: res.append(0)

        print(res)
        print("Оптимальный план:", (-1)*round(lim_coef_st[-1][-1]))
        break

    print(numNotInt)
    print('\n')

    maxDrob = -1
    maxDrobNum = -1

    for i in numNotInt:
        if NotInt[i] % 1 > maxDrob:
            maxDrob = NotInt[i] % 1
            maxDrobNum = i
    print(maxDrobNum)
    print('')

    newStr = []
    for i in range(len(lim_coef_st[maxDrobNum])):
        newStr.append((lim_coef_st[maxDrobNum][i] % 1)*(-1))

    newStr.append(1)
    newStr[-1],newStr[-2] = newStr[-2],newStr[-1]
    print(newStr)
    print('')

    for i in range(len(lim_coef_st)):
        lim_coef_st[i].append(0)
        lim_coef_st[i][-1], lim_coef_st[i][-2] = lim_coef_st[i][-2], lim_coef_st[i][-1]
    lim_coef_st.append(newStr)
    lim_coef_st[-1], lim_coef_st[-2] = lim_coef_st[-2], lim_coef_st[-1]
    if (chekerer == 0):
        for i in range(len(lim_coef_st[-1])):
            lim_coef_st[-1][i] *= -1
    for i in range(len(lim_coef_st)):
        print(lim_coef_st[i])
    print('')

    #Таблица для гомори готова

    flag = 1

    resh_Coef = 10000000

    #решающая строка
    resh_Str = len(lim_coef_st) - 2
    print(resh_Str)
# решающий столбец
    for i in range(len(lim_coef_st[-1])):
        if lim_coef_st[-2][i] == 0:
            err_full_skip = err_full_skip + 1
            continue
        if lim_coef_st[-1][i] == 0:
            err_full_skip = err_full_skip + 1
            continue
        if (lim_coef_st[-1][i] / lim_coef_st[-2][i] < resh_Coef):
            resh_Coef = lim_coef_st[-1][i] / lim_coef_st[-2][i]
            resh_Stol = i
        if (err_full_skip == len(right_part)): raise SystemExit("Невозможно найти оптимальный план столбец")
        err_full_skip = 0

    print(resh_Stol)
    print('')


    resh_Coef = 10000000


    resh_Elem = lim_coef_st[resh_Str][resh_Stol]
    print(resh_Elem)

    # копирование матрицы коэффициентов
    lim_coef_prev = copy.deepcopy(lim_coef_st)

    #деление строки на решающий элемент
    for i in range(len(lim_coef_st[-2])):
        lim_coef_st[-2][i] = lim_coef_prev[-2][i] / resh_Elem

    # зануление решающего столбца
        for i in range(len(lim_coef_st)):
            if (i != resh_Str):
                lim_coef_st[i][resh_Stol] = 0.0

    # метод прямоугольника
        for i in range(len(lim_coef_prev)):
            if (i == resh_Str): continue
            for j in range(len(lim_coef_prev[i])):
                if (j == resh_Stol): continue
                lim_coef_st[i][j] = lim_coef_prev[i][j] - lim_coef_prev[resh_Str][j] * lim_coef_prev[i][resh_Stol] / lim_coef_prev[resh_Str][resh_Stol]

    #пересчитаная таблица
    for i in range(len(lim_coef_st)):
        print(lim_coef_st[i])
    print('')
    chekerer += 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
