import multiprocessing
import os
import random
from multiprocessing import Process
from typing import List

from RandomWordGenerator import RandomWord


def rand(n, num):
    rw = RandomWord()
    rw.constant_word_size = False
    filename = f"./result_files/Process-{num}-{os.getpid()}.txt"
    try:
        with open(filename, "a") as file:
            for i in range(n):
                file.write(f'{rw.generate()}\n')
        get_analiz1(filename)
        # get_analiz2(filename)
    except Exception:
        pass


if __name__ == '__main__':
    manager = multiprocessing.Manager()

    try:
        list_process: List[Process] = []

        for i in range(1, multiprocessing.cpu_count() + 1):
            name_pr: str = f'pr{i}'
            r: int = random.randint(100000, 5000000)
            process = Process(target=rand, args=(r, i), name=name_pr)
            list_process.append(process)
            process.start()

        for i in range(1, multiprocessing.cpu_count() + 1):
            list_process[i].join()
    except Exception:
        pass


def read(file):
    file = open(file, 'r')
    k = 0
    for line in file:
        k += 1
    file.close()
    return k


def get_all(file):
    try:
        file = open(f'{file}', 'r')
        number: int = 0
        for line in file:
            for sim in line:
                if sim != '\n':
                    number += len(sim)
        return number
    except Exception:
        pass
    finally:
        file.close()


def get_max(file: str):
    file = open(file, 'r')
    maxlenth: int = -1
    for line in file:
        line = line.replace("\n", "")
        if line != '':
            if maxlenth == -1:
                maxlenth = len(line)
            else:
                if maxlenth < len(line):
                    maxlenth = len(line)
    file.close()
    return maxlenth


def get_min(file: str):
    file = open(file, 'r')
    minlenth: int = -1
    for line in file:
        line = line.replace("\n", "")
        if line != '':
            if minlenth == -1:
                minlenth = len(line)
            else:
                if minlenth > len(line):
                    minlenth = len(line)
    file.close()
    return minlenth


def get_sred(file: str):
    sred: int = get_all(file) / read(file)
    return sred


def get_glasn_and_sogl(file):
    glasn: int = 0
    sogl: int = 0
    symbols: list = ['a', 'e', 'i', 'o', 'u', 'y']
    with open(f'{file}', 'r') as file1:
        for line in file1.readlines():
            line.lower()
            for sim in line:
                if sim in symbols:
                    glasn += 1
                else:
                    sogl += 1

    return [glasn, sogl]


def get_sl2(file: str):
    file = open(file, 'r')
    list_file: List[str] = file.read().split()
    diction: dict = dict()

    for word in list_file:
        if len(word) in diction:
            diction[len(word)] += 1
        else:
            diction[len(word)] = 1

    sorted_dict = {}
    sorted_keys = sorted(diction.keys())

    for w in sorted_keys:
        sorted_dict[w] = diction[w]
    rep_dict = sorted_dict.copy()

    rep: str = ""
    for key in diction:
        rep += f"   * {key} симв. >> {diction[key]} повторений.\n"
    file.close()
    return rep


def get_analiz1(file):
    listr1 = get_glasn_and_sogl(file)
    return print(f"********************************************************\n"
                 f"  Аналитика для файла {file}\n"
                 f"********************************************************\n"
                 f"  1. Всего символов --> {get_all(file)}\n"
                 f"  2. Максимальная длина слова --> {get_max(file)}\n"
                 f"  3. Минимальная длина слова --> {get_min(file)}\n"
                 f"  4. Средняя длина слова --> {get_sred(file)}\n"
                 f"  5. Количество гласных --> {listr1[0]}\n"
                 f"  6. Количсетво согласных --> {listr1[1]}\n"
                 f"  7. Количество повторений слов с одинаковой длиной:\n{get_sl2(file)}")
