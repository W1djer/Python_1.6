# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу

import random
array = []
for i in range(16):
    array.append(random.randint(1, 11))
print(array)
couple = 0
for i in range(len(array)-1):
    for j in range(i+1, len(array)):
        if array[i] == array[j]:
            couple += 1
print("Количество пар:",couple)