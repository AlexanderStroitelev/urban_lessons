import sqlite3


conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Удаляем таблицу, если она уже существует
cursor.execute('DROP TABLE IF EXISTS Users')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

users_data = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000)
]

cursor.executemany('''
INSERT INTO Users (username, email, age, balance)
VALUES (?, ?, ?, ?)
''', users_data)

# Обновляем balance у каждой 2ой записи начиная с 1ой на 500
cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")

# Удаляем каждую 3ю запись начиная с 1ой
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

# Выборка всех записей, где возраст не равен 60
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
results = cursor.fetchall()

# Удаляем пользователя с id=6
cursor.execute("DELETE FROM Users WHERE id = 6")

# Подсчет количества всех пользователей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

# Подсчет суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

# Вычисление среднего баланса
average_balance = all_balances / total_users if total_users > 0 else 0

# Вывод среднего баланса в консоль
print(average_balance)

# Закрываем соединение с базой данных
conn.commit()
conn.close()
