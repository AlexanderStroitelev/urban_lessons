import numpy as np
import pandas as pd
import requests


def demonstrate_requests():
    print("\n=== Демонстрация requests ===")

    response = requests.get("https://api.github.com/repos/python/cpython")

    print(f"1. Статус код запроса: {response.status_code}")
    print(f"2. Тип контента: {response.headers['content-type']}")

    data = response.json()

    print(
        f"3. Информация о репозитории:\n"
        f"   - Название: {data['name']}\n"
        f"   - Звезд: {data['stargazers_count']}\n"
        f"   - Описание: {data['description']}"
    )


def demonstrate_pandas():
    print("\n=== Демонстрация pandas ===")

    data = {
        "Имя": ["Анна", "Борис", "Владимир", "Галина"],
        "Возраст": [25, 32, 45, 28],
        "Зарплата": [50000, 65000, 85000, 55000],
    }
    df = pd.DataFrame(data)

    print("1. Созданный DataFrame:")
    print(df)
    print("\n2. Статистический анализ числовых столбцов:")
    print(df.describe())
    print("\n3. Средняя зарплата по возрастным группам:")
    df["Возрастная_группа"] = pd.cut(
        df["Возраст"], bins=[0, 30, 40, 50], labels=["20-30", "31-40", "41-50"]
    )
    print(df.groupby("Возрастная_группа", observed=True)["Зарплата"].mean())


def demonstrate_numpy():
    print("\n=== Демонстрация numpy ===")

    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.linspace(0, 1, 5)  # 5 чисел от 0 до 1

    print("1. Созданные массивы:")
    print(f"arr1: {arr1}")
    print(f"arr2: {arr2}")

    print("\n2. Математические операции:")
    print(f"Умножение массивов: {arr1 * arr2}")
    print(f"Синус arr1: {np.sin(arr1)}")

    print("\n3. Статистические функции:")
    print(f"Среднее arr1: {np.mean(arr1)}")
    print(f"Стандартное отклонение arr1: {np.std(arr1)}")
    matrix = np.random.rand(3, 3)

    print("\n4. Случайная матрица 3x3:")
    print(matrix)

    print(f"\nОпределитель матрицы: {np.linalg.det(matrix):.2f}")


if __name__ == "__main__":
    demonstrate_requests()
    demonstrate_pandas()
    demonstrate_numpy()


# Выводы:
# - Requests
# Эта библиотека позволила нам легко и удобно отправлять HTTP-запросы, обрабатывать параметры,
# заголовки и анализировать ответы. Использование requests расширяет стандартные возможности
# Python для взаимодействия с сетью, упрощая работу с API и загрузку данных.
#
# - Pandas
# С помощью pandas мы получили доступ к мощным инструментам для обработки табличных данных:
# чтение файлов, статистический анализ и группировка данных стали быстрыми и интуитивно
# понятными. Это делает библиотеку незаменимой в аналитике данных.
#
# - Numpy
# Numpy значительно упростила выполнение сложных математических операций над массивами данных.
# Высокая производительность и удобство работы делают её базовым инструментом для вычислений
# в Python.
#
# Использование этих библиотек позволило расширить возможности Python для работы с данными,
# автоматизации задач и научных вычислений.
