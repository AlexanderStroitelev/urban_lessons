def add_everything_up(a, b):
    try:
        # Пытаемся сложить a и b
        result = a + b
    except TypeError:
        # Если происходит TypeError (разные типы), возвращаем строковое представление a и b
        result = str(a) + str(b)
    return result


# Примеры использования
print(add_everything_up(123.456, 'строка'))  # Ожидаемый результат: '123.456строка'
print(add_everything_up('яблоко', 4215))     # Ожидаемый результат: 'яблоко4215'
print(add_everything_up(123.456, 7))         # Ожидаемый результат: 130.456