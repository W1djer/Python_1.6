# Заполните массив элементами арифметической прогрессии.

a = int(input("Введите первое число:"))
b = int(input("Введите шаг:"))
d = int(input("Введите количество элементов:"))
mas =[]
for i in range(d):
    mas.append(a)
    a += b
print(mas)