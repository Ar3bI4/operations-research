# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import copy
func_coef = [5,2] # коэф в функционале
lim_coef = [ # коэф в ограничениях
    [1,2],
    [2,1],
    [-1,1],
    [0,1]
]
right_part = [6,8,1,2] # вектор В
Z = [] # индексная сторока
optium = 0 # свободный член

for i in range(len(right_part)):# смена знака неравенства в ограничениях на канонический
    if (right_part[i] < 0):
        right_part[i] =  (-1)*right_part[i]
        for j in range(len(func_coef)):# смена знака значений
            lim_coef[i][j] = (-1)*lim_coef[i][j]

for j in range(len(func_coef)):# добавление коэффициентов функционала в индексную строку
    Z.append((-1) * func_coef[j])
for j in range(len(lim_coef)):# добавление нулей у базисных переменных в индексную строку
    Z.append(0)
print('Индексная строка: ')
print(Z)
# добавление базисных переменных S
for i in range(len(lim_coef)):
    for j in range(len(lim_coef)):
        if (i == j):
            lim_coef[i].append(1)
        else: lim_coef[i].append(0)

# вывод для проверки
print("Первая симплекс таблица:")
for j in range(len(lim_coef)):
    print(lim_coef[j])
print(right_part)
print(Z)

print("Задача на: 1 - минимум, 2 - максимум")
x = int(input())
Z_new = Z.copy()
if(x == 1):
    # проверка оптимальности для минимума
    while 1:
        k=0
        for i in range (len(Z)):
            if (Z_new[i]>0): k+=1# проверка наличия в индексной строке положительных значений
        if(k==0):# если все значения в индексной строке не положительные
            print("найден оптимальный план на мининум")
            opt_plan = []
            q = 0
            for i in range(len(Z)):
                if (Z[i] == 0):
                    opt_plan.append(right_part[q])# добавление значений базисных переменных в оптимальный план
                    q = q + 1
                else:
                    opt_plan.append(0)# добавление нулей в значения небазисных переменных в оптимальный план
            print(opt_plan)
            exit()
        else:# если в индексной строке есть положительные значения
            #print(Z)
            maxz = abs(Z[0])
            maxi = 0
            for i in range(len(Z)):# поиск максимального по модулю элемента в индексной строке
                if ((abs(Z[i]) > maxz) and (Z[i] > 0)):
                    maxz = abs(Z[i])
                    maxi = i# индекс максимального элемента
            #print(maxi)

            solve_col = []
            for i in range(len(lim_coef)):#
                for j in range(len(lim_coef) + len(func_coef)):
                    if (j == maxi):
                        solve_col.append(lim_coef[i][j])# заполнение решающего столбца
            print("Разрешаюший столбец:")
            print(solve_col)
            n = 0
            for i in range(len(solve_col)):
                if (solve_col[i] <= 0): n += 1
            if(n > 0):
                print("Error")
                exit()

            tmp = []
            for i in range(len(solve_col)):
                if (solve_col[i] == 0):
                    tmp.append(right_part[i] * 1000)
                else:
                    tmp.append(right_part[i] / solve_col[i])# значения индексного столбца, делённые на значения разрешающего столбца
            #print(tmp)
            for i in range(len(tmp)):
                if ((tmp[i] < 0)):
                    tmp[i] = tmp[i] * -1000
            mint = tmp[0]
            mini = 0
            for i in range(len(tmp)):# выбор индекса разрешающей строки
                if ((tmp[i] < mint)):
                    mint = tmp[i]
                    mini = i
            #print(mini)

            solve_el = lim_coef[mini][maxi]
            print("Разрешаюший элемент:")
            print(solve_el)

            lim_coef_new = copy.deepcopy(lim_coef)

            # правило прямоугольника
            for i in range(len(lim_coef_new)):
                if (i != mini):
                    for j in range(len(lim_coef_new) + len(func_coef)):
                        if (j != maxi):
                            lim_coef_new[i][j] = lim_coef[i][j] - ((lim_coef[i][maxi] * lim_coef[mini][j]) / solve_el)

            lim_coef_new[mini][maxi] = 1# новое значение разрешающего элемента

            for i in range(len(lim_coef_new)):
                if (i != mini):
                    lim_coef_new[i][maxi] = 0# новые значения в разрешающем столбце

            for j in range(len(lim_coef_new) + len(func_coef)):
                if (j != maxi):
                    lim_coef_new[mini][j] = lim_coef[mini][j] / solve_el# новые значения в разрешающей строке
            print("Пересчитанная симплекс таблица:")
            for j in range(len(lim_coef_new)):
                print(lim_coef_new[j])

            Z_new = Z.copy()
            Z_new[maxi] = 0# пересчёт значения разрешающего столбца в индексной строке
            for i in range(len(Z_new)):
                if (i != maxi):
                    Z_new[i] = Z[i] - ((Z[maxi] * lim_coef[mini][i]) / solve_el)# пересчёт значений индексной строки
            print(Z_new)

            right_part_new = right_part.copy()
            right_part_new[mini] = right_part_new[mini] / solve_el# пересчёт значения разрешающей строки в индексном столбце
            for i in range(len(right_part_new)):
                if (i != mini):
                    right_part_new[i] = right_part[i] - ((right_part[mini] * lim_coef[i][maxi]) / solve_el)# пересчёт значений индексного столбца
            n = 0
            for i in range(right_part_new[i]):
                if (right_part_new[i] < 0): n += 1
            if (n > 0):
                print("Error")
                exit()

            print(right_part_new)
            optium = optium - ((right_part[mini] * Z[maxi]) / solve_el)# пересчёт значения оптимума
            print("Оптимум:")
            print(optium)

            lim_coef = copy.deepcopy(lim_coef_new)
            Z = Z_new.copy()
            right_part = right_part_new.copy()
elif(x == 2):
    # проверка оптимальности для максимума
    while 1 :
        k=0
        for i in range (len(Z)):
            if (Z_new[i]<0): k+=1# проверка наличия в индексной строке отрицательных значений
        if(k==0):# если все значения в индексной строке не отрицательные
            print("найден оптимальный план(максимум)")
            opt_plan = []
            q = 0
            for i in range(len(Z)):
                if (Z[i] == 0):
                    opt_plan.append(right_part[q])# добавление значений базисных переменных в оптимальный план
                    q=q+1
                else:
                    opt_plan.append(0)# добавление нулей в значения небазисных переменных в оптимальный план
            print(opt_plan)
            exit()
        else:# если в индексной строке есть отрицательные значения
            #print(Z)
            maxz = abs(Z[0])
            maxi = 0
            for i in range(len(Z)):
                if ((abs(Z[i]) > maxz) and (Z[i]<0)):# поиск максимального отрицательного по модулю элемента в индексной строке
                    maxz = abs(Z[i])
                    maxi = i# индекс максимального отрицательного элемента
            #print(maxi)

            solve_col = []
            for i in range(len(lim_coef)):
                for j in range(len(lim_coef)+ len(func_coef)):
                    if (j == maxi):
                        solve_col.append(lim_coef[i][j])# заполнение решающего столбца
            print("Разрешаюший столбец:")
            print(solve_col)

            n = 0
            for i in range(len(solve_col)):
                if (solve_col[i] < 0): n += 1
            if(n > 0):
                print("Error")
                exit()

            tmp = []
            for i in range(len(solve_col)):
                if (solve_col[i] == 0):
                    tmp.append(right_part[i]*1000)
                else:
                    tmp.append(right_part[i] / solve_col[i])# значения индексного столбца, делённые на значения разрешающего столбца
            #print(tmp)
            for i in range(len(tmp)):
                if ((tmp[i] < 0)):
                    tmp[i]= tmp[i]*-1000
            mint = tmp[0]
            mini = 0
            for i in range(len(tmp)):
                if ((tmp[i] < mint)):
                    mint = tmp[i]# выбор индекса разрешающей строки
                    mini = i
            #print(mini)

            solve_el = lim_coef[mini][maxi]
            print("Разрешаюший элемент:")
            print(solve_el)

            lim_coef_new = copy.deepcopy(lim_coef)

            # правило прямоугольника
            for i in range(len(lim_coef_new)):
                if (i != mini):
                    for j in range(len(lim_coef_new) + len(func_coef)):
                        if (j != maxi):
                            lim_coef_new[i][j] = lim_coef[i][j] - ((lim_coef[i][maxi] * lim_coef[mini][j]) / solve_el)

            lim_coef_new[mini][maxi] = 1# новое значение разрешающего элемента

            for i in range(len(lim_coef_new)):
                if (i != mini):
                    lim_coef_new[i][maxi] = 0# новые значения в разрешающем столбце

            for j in range(len(lim_coef_new) + len(func_coef)):
                if (j != maxi):
                    lim_coef_new[mini][j] = lim_coef[mini][j] / solve_el# новые значения в разрешающей строке

            print("Пересчитанная симплекс таблица:")
            for j in range(len(lim_coef_new)):
                print(lim_coef_new[j])

            Z_new = Z.copy()

            Z_new[maxi] = 0# пересчёт значения разрешающего столбца в индексной строке
            for i in range(len(Z_new)):
                if (i != maxi):
                    Z_new[i] = Z[i] - ((Z[maxi] * lim_coef[mini][i]) / solve_el)# пересчёт значений индексной строки
            print(Z_new)

            right_part_new = right_part.copy()
            right_part_new[mini] = right_part_new[mini] / solve_el# пересчёт значения разрешающей строки в индексном столбце
            for i in range(len(right_part_new)):
                if (i != mini):
                    right_part_new[i] = right_part[i] - ((right_part[mini] * lim_coef[i][maxi]) / solve_el)# пересчёт значений индексного столбца
            print(right_part_new)
            n = 0
            for i in range(right_part_new[i]):
                if (right_part_new[i] < 0): n += 1
            if (n > 0):
                print("Error")
                exit()

            optium = optium - ((right_part[mini] * Z[maxi]) / solve_el)# пересчёт значения оптимума
            print("Оптимум:")
            print(optium)
            # if (optium < 0):
            #     print("Error")
            #     exit()

            lim_coef = copy.deepcopy(lim_coef_new)
            Z = Z_new.copy()
            right_part = right_part_new.copy()

else:
    print("wrong input")
    exit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
