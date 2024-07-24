first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(s1) - len(s2)) for s1, s2 in zip(first, second) if len(s1) != len(s2))
second_result = (s1 == s2 for i in range(len(first)) for s1, s2 in [(first[i], second[i])])

print(list(first_result))
print(list(second_result))
