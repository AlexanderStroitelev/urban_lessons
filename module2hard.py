number = int(input("Введите число от 3 до 20: "))

divisors = []
pairs = []

if 3 <= number <= 20:
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)

    for i in divisors:
        for j in range(1, i // 2 + 1):
            k = i - j
            if (j, k) not in pairs and (k, j) not in pairs and j != k:
                pairs.append((j, k))

    pairs.sort()

    result = "".join([str(pair_element) for pair in pairs for pair_element in pair])
    print(result)
else:
    print("Введенное число не находится в диапазоне от 3 до 20.")
