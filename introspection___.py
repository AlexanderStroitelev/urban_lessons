import inspect
from pprint import pprint


def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты и методы объекта
    attributes = []
    methods = []

    # Проходим по всем элементам объекта
    for item in dir(obj):
        # Проверяем, является ли элемент атрибутом или методом
        if callable(getattr(obj, item)):
            methods.append(item)
        else:
            attributes.append(item)

    # Получаем модуль, к которому принадлежит объект
    module = inspect.getmodule(obj)
    module_name = module.__name__ if module else None

    # Формируем и возвращаем словарь с результатами
    return {
        "type": obj_type,
        "attributes": attributes,
        "methods": methods,
        "module": module_name,
    }


# Пример использования
number_info = introspection_info(42)
pprint(number_info)
