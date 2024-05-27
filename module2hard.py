number = int(input("Пожалуйста, введите число от 3 до 20: "))
if 3 <= number <= 20:
    merged_pairs = []
    for i in range(2, number + 1):
        if number % i == 0:
            pairs = []
            for j in range(1, i):
                k = i - j
                if j < k:
                    is_duplicate = False
                    for pair in pairs:
                        if (j, k) == pair or (k, j) == pair:
                            is_duplicate = True
                            break
                    if not is_duplicate:
                        pairs.append((j, k))
            merged_pairs.extend(pairs)

    merged_pairs.sort()

    result = ''.join(str(pair_element) for pair in merged_pairs for pair_element in pair)
    print(result)
else:
    print("Введенное число не находится в диапазоне от 3 до 20.")