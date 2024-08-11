import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()


if __name__ == '__main__':
    # путь к папке Files
    filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

    # линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f"Линейное выполнение: {linear_duration:.6f} секунд")

    # многопроцессный вызов
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    multiprocess_duration = time.time() - start_time
    print(f"Многопроцессное выполнение: {multiprocess_duration:.6f} секунд")
