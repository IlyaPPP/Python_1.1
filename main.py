""" 1 Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка,
стоящих на нечётной позиции.
*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 """

numbers = []
summ = 0
n = 5

print(f'Введите {n} чисел: ')
for i in range(n):
        numbers.append(int(input()))

for i in range(n):
    if i%2 != 0:
        summ += numbers[i]

print(summ)