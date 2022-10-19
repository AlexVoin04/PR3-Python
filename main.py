import multiprocessing
import os
import random
from multiprocessing import Process, Pool
from RandomWordGenerator import RandomWord


def rand(n, m):
    rw = RandomWord()
    filename = f"C:\\Alex\\PythonProject\\PR3\\result_files\\Process-{m}-{os.getpid()}.txt"
    with open(filename, "a") as file:
        for i in range(n):
            file.write(rw.generate())

    summa: int = 0
    maxdlin: int = 0
    with open(file1, 'w') as file:
        maxdlin = max(file, key = len)
        with open(file1, 'w') as file:
            mindlin = min(file, key=len)
        for i in file:
            summa += i.len()

    print("********************************************************")
    print(f"  Аналитика для файла {filename}")
    print("********************************************************")
    print(f"{sum}\n{len(maxdlin)}\n{len(mindlin)-1}")


for i in range(1, multiprocessing.cpu_count() + 1):
    r: int = random.randint(100000, 5000000)
    process = Process(target=rand, args=(r, i))
    process.start()
    process.join()
