# Создание модуля fake_math
def divide(first, second):
    if second == 0:
        return 'Ошибка'
    return first / second

____________________________________________________________________

# Создание модуля true_math
from math import inf
def divide(first, second):
    if second == 0:
        return inf
    return first / second

____________________________________________________________________

# Создание модуля main
from fake_math import divide as fake_divide
from true_math import divide as true_divide

x = int(input('Введите число 1 для fake_divide:'))
y = int(input('Введите число 2 для fake_divide:'))
a = int(input('Введите число 1 для true_divide:'))
b = int(input('Введите число 2 для true_divide:'))
# Тестирование функций divide
result_fake = fake_divide(x, y)
result_true = true_divide(a, b)

# Вывод результатов на экран
print(result_fake)
print(result_true)
