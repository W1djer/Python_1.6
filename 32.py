# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону

import random
array = []
for i in range(16):
    array.append(random.randint(-15, 16))
print("Массив: ",array)
min = -5
max = 5
mas = []
for i in range(len(array)):
    if min < array[i] < max:
        mas.append(i)
print("Индексы элементов в диапазоне от {} до {}:  {}".format(min, max, mas))