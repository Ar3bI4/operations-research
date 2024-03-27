# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import copy
a = int(input("0 - Минимум  1 - Максимум"))
func_coef = [5, 2] #коэфы в функционале
lim_coef_st = [ #коэфы в ограничениях (потом преобразуется в lim_coef1)
    [2, 1, 0, 0, 0],
    [4, 3, 0, -1, 0],
    [1, 2, 0, 0, 1]
]
lim_coef = []
right_part = [2, 5, 4] #вектор В
Z = [] #самая нижняя сторочка
resh_Str = 0
resh_Stol = 0
resh_Coef = 10000000
resh_Elem = 0
max_Z = 0
min_Z = 0
flag = 1
numberR = []


for j in range(len(func_coef)):
    Z.append((-1)*func_coef[j])
for j in range(len(lim_coef_st)):
    Z.append(0)
    Z.append(0)

if (a ==0):
    M = 10000
if (a == 1):
    M = -10000

for i in range(len(lim_coef_st)):
    if(right_part[i] < 0):#неравенства
        for k in range(len(lim_coef_st[i])):
            lim_coef_st[i][k] = lim_coef_st[i][k] * (-1)
        right_part[i] = right_part[i] * (-1)
    lim_coef.append([])
    for j in range(len(lim_coef_st[i])):
        lim_coef[i].append(lim_coef_st[i][j])

# вывод для проверки
for j in range(len(lim_coef)):
    print(lim_coef[j])
print(Z)
print(' ')
#print(lim_coef[0])

#добавление 1 и 0 для R
for i in range(len(lim_coef)):
        for j in range(len(lim_coef)):
            if (i == j):
                lim_coef[i].append(1)
            else: lim_coef[i].append(0)

print(lim_coef)
print(lim_coef[0])
print(' ')
summ = 0
print(len(lim_coef[0])-len(lim_coef))

for i in range(len(lim_coef[0])-len(lim_coef)):#вывод штрафов
    for j in range(len(lim_coef)):
        summ = summ + lim_coef[j][i]
    print(summ)
    Z[i] = Z[i] + summ*M
    summ = 0


srp=0
for i in range(len(right_part)):#штраф в значении оптимума
    srp = srp + right_part[i]
Z.append(M*srp)

# вывод для проверки
for j in range(len(lim_coef)):
    print(lim_coef[j])
print(Z)
print(' ')

#решающий столбец
for i in range(len(Z)-1):
    if (a == 0):
        if (Z[i] > 0) and (abs(Z[i]) > abs(max_Z)):#для минимума
            max_Z = Z[i]
            resh_Stol = i
    if (a == 1):
        if (Z[i] < 0) and (abs(Z[i]) > abs(max_Z)):#для максимума
            max_Z = Z[i]
            resh_Stol = i
print(resh_Stol)

max_Z = 0
err_full_skip = 0#переменная ошибки поиска разрешающей строки
#оптимальный план
opt_pl = []
for i in range(len(Z)-1):
    opt_pl.append(0)

#решающя строка
for i in range(len(right_part)):
    if lim_coef[i][resh_Stol] <= 0:
        err_full_skip = err_full_skip + 1
        continue
    if right_part[i] == 0:
        err_full_skip = err_full_skip + 1
        continue
    if (right_part[i] / lim_coef[i][resh_Stol] < resh_Coef):#выбор решающей строки
        resh_Coef = right_part[i] / lim_coef[i][resh_Stol]
        resh_Str = i
if (err_full_skip == len(right_part)): raise SystemExit("Невозможно найти оптимальный план")
err_full_skip = 0

print(resh_Stol)
print('')

resh_Coef = 10000000

resh_Elem = lim_coef[resh_Str][resh_Stol]#решающий элемент


#копирование матрицы коэффициентов

lim_coef_prev = []
lim_coef_cur = []
for i in range(len(lim_coef)):
    lim_coef[i].append(right_part[i])#добавление правого столбца в матрицу
lim_coef.append(Z)

lim_coef_prev = copy.deepcopy(lim_coef)
lim_coef_cur = copy.deepcopy(lim_coef)

temp = 0

# вывод для проверки
for j in range(len(lim_coef)):
    print(lim_coef[j])
print(resh_Str)
print(resh_Stol)


#Максимум
if (a == 1):
    while (flag != 0):
        flag = 0
        if (temp != 0):
            # решающий столбец
            for i in range(len(Z)-1):
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
            if (err_full_skip == len(right_part)): raise SystemExit("Невозможно найти оптимальный план")
            err_full_skip = 0

        print(resh_Str)
        print(resh_Stol)
        resh_Elem = lim_coef_prev[resh_Str][resh_Stol]

        #деление решающей строки на решающий элемент
        for i in range(len(lim_coef[1])):
            lim_coef_cur[resh_Str][i] = lim_coef_cur[resh_Str][i]/resh_Elem

        #зануление решающего столбца
        for i in range(len(right_part)+1):
            if (i != resh_Str):
                lim_coef_cur[i][resh_Stol] = 0

        #метод прямоугольника
        for i in range(len(lim_coef_prev)):
            if (i == resh_Str):continue
            for j in range(len(lim_coef_prev[i])):
                if (j == resh_Stol):continue
                lim_coef_cur[i][j] = lim_coef_prev[i][j] - lim_coef_prev[resh_Str][j] *  lim_coef_prev[i][resh_Stol] / lim_coef_prev[resh_Str][resh_Stol]


        Z = copy.deepcopy(lim_coef_cur[len(lim_coef_cur)-1])
        for i in range(len(lim_coef_cur)-1):
            right_part[i] = lim_coef_cur[i][len(lim_coef_cur[i])-1]

        #проверка
        for i in range(len(lim_coef_cur[len(lim_coef_prev)-1])-1):
            if (lim_coef_cur[len(lim_coef_cur)-1][i] < 0):
                flag = 1

        lim_coef_prev = copy.deepcopy(lim_coef_cur)

        temp = temp + 1
    # вывод для проверки
        for j in range(len(lim_coef_cur)):
            print(lim_coef_cur[j])
    print("")
    print("")

#Минимум
if (a == 0):
    while (flag != 0):
        flag = 0
        if (temp != 0):
            # решающий столбец
            for i in range(len(Z)-1):
                if (Z[i] > 0) and (abs(Z[i]) > abs(max_Z)):
                    max_Z = Z[i]
                    resh_Stol = i
            max_Z = 0

            # решающя строка
            for i in range(len(right_part)):
                if lim_coef_prev[i][resh_Stol] <= 0:
                    err_full_skip = err_full_skip +1
                    continue
                if right_part[i] == 0:
                    err_full_skip = err_full_skip +1
                    continue
                if (right_part[i] / lim_coef_prev[i][resh_Stol] < resh_Coef):
                    resh_Coef = right_part[i] / lim_coef_prev[i][resh_Stol]
                    resh_Str = i
            if (err_full_skip == len(right_part)): raise SystemExit("Невозможно найти оптимальный план")
            err_full_skip = 0
            resh_Coef = 10000000

        resh_Elem = lim_coef_prev[resh_Str][resh_Stol]
        #деление решающей строки на решающий элемент
        for i in range(len(lim_coef[1])):
            lim_coef_cur[resh_Str][i] = lim_coef_cur[resh_Str][i]/resh_Elem

        #зануление решающего столбца
        for i in range(len(right_part)+1):
            if (i != resh_Str):
                lim_coef_cur[i][resh_Stol] = 0

        #метод прямоугольника
        for i in range(len(lim_coef_prev)):
            if (i == resh_Str):continue
            for j in range(len(lim_coef_prev[i])):
                if (j == resh_Stol):continue
                lim_coef_cur[i][j] = lim_coef_prev[i][j] - lim_coef_prev[resh_Str][j] *  lim_coef_prev[i][resh_Stol] / lim_coef_prev[resh_Str][resh_Stol]


        Z = copy.deepcopy(lim_coef_cur[len(lim_coef_cur)-1])
        for i in range(len(lim_coef_cur)-1):
            right_part[i] = lim_coef_cur[i][len(lim_coef_cur[i])-1]

        #проверка
        for i in range(len(lim_coef_cur[len(lim_coef_prev)-1])-1):
            if (lim_coef_cur[len(lim_coef_cur)-1][i] > 0):
                flag = 1

        lim_coef_prev = copy.deepcopy(lim_coef_cur)

        temp = temp + 1

        #вывод для проверки
        for j in range(len(lim_coef_cur)):
            print(lim_coef_cur[j])
        print(resh_Str)
        print(resh_Stol)
    print("")
    print("")


for i in range(len(right_part)):
    for j in range(len(lim_coef_cur[i])-1):
        if (lim_coef_cur[i][j] == 1):
            opt_pl[j] = right_part[i]#определение значений оптимального плана

for i in range(len(right_part)):
    opt_pl.pop(len(opt_pl)-1)

check = 0
for i in range(len(opt_pl)-len(right_part), len(opt_pl)):
    if (opt_pl[i] > 0):
        check += 1

#if (check == 0):raise SystemExit("Есть R в базисе")#ошибка R в базисе
print("Оптимальный план:", opt_pl)
print("Оптимум:", lim_coef_cur[len(lim_coef_cur)-1][len(lim_coef_cur[len(lim_coef_cur)-1])-1])



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
