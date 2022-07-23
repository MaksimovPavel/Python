#Сумма чисел вещестаенного числа
#1 вариант
'''
stroka = input()
summa = 0
for i in stroka:
    if i != '.':
        summa = summa + int(i)
print(summa)
#2 вариант
stroka = input()
summa = 0
for i in stroka:
    if i.isdigit():
        summa = summa + int(i)
print(summa)

# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
stroka = ' 267 12 963'
list_1 = stroka.split()
max = int(list_1[0])
min = int(list_1[0])
for i in list_1:
    if int(i) > max:
        max = int(i)
    if int(i) < max:
        min = int(i)
print(max)
print(min)

#Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:


a = float(input('Введите A'))
b = float(input('Введите B'))
c = float(input('Введите С'))
x1=0
x2=0
D = b **2 - 4 * a * c
if D == 0:
    print(f'Один корень и он равен = {round(-b/2)}')
elif D < 0:
    print('Корней нет')
else:
    print(f'первый корень равен = {(- b + D ** 0.5)/(2 * a), 2}')
    print(f'второй корень равен = {(- b - D ** 0.5)/(2 * a), 2}')


# найти наименьшее общее кратное
a = int(input())
b = int(input())
s = a * b
while a != b:
    if a > b:
        a -= b
    else:
        b -=a
print( s // a)

#1
with open('1.txt', 'r', encoding='utf-8') as file:
    arr = file.readlines()
    arr = [int(i) for i in arr[0].split()]
    for i in range(1, len(arr)):
        if arr[i] - 1 != arr[i - 1]:
            print((arr[i - 1] + arr[i]) // 2)
'''
