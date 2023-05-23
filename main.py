""" Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]* """

numbers = []
prod = 0
n = 5

if n%2 == 0:
    s = n // 2
else:
    s = (n // 2) + 1

print(f'Введите {n} чисел: ')

for i in range(n):
    numbers.append(int(input()))

for i in range(s):
    prod = numbers[i] * numbers[n-i-1]
    print(prod)
    prod = 0