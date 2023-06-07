# Даны два массива чисел. Требуется вывести те элементы первого массива, которых нет во втором массиве.

import random
def array(a):
    array = []
    for i in range(a):
        array.append(random.randint(1, 21))
    return array
n = int(input("Введите количество элементов первого массива: "))
m = int(input("Введите количество элементов второго массива: "))
mas1 = array(n)
mas2 = array(m)
mas3 = []
print("Первый массив:",mas1)
print("Второй массив:",mas2)
for i in mas1:
    flag = True
    for j in mas2:
        if i == j:
            flag = False
    if flag == True:
        mas3.append(i)
print(mas3)