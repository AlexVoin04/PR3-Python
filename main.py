import multiprocessing
import os
import random
from multiprocessing import Process, Pool
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
        get_analiz2(filename)
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


def get_min(file):
    m: str = ""
    with open(f'{file}', 'r') as file1:
        m = min(file1, key=len)
    return len(m) - 1


def get_max(file):
    m: str = ""
    with open(f'{file}', 'r') as file1:
        m = max(file1, key=len)
    return len(m) - 1


def get_all(file):
    try:
        file = open(f'{file}', 'r')
        data = file.read()
        number: int = len(data)
        return number
    except Exception:
        pass
    finally:
        file.close()


def get_kolvo(file):
    try:
        file = open(f'{file}', 'r')
        data = file.read()
        words = data.split()
        return len(words)
    except Exception:
        pass
    finally:
        file.close()


def get_sred(file):
    try:
        file = open(f'{file}', 'r')
        data = file.read()
        words = data.split()
        number = len(data)
        sred = number / len(words)
        return sred
    except Exception:
        pass
    finally:
        file.close()


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


def get_analiz1(file):
    listr1 = get_glasn_and_sogl(file)
    return print(f"********************************************************\n"
                 f"  ?????????????????? ?????? ?????????? {file}\n"
                 f"********************************************************\n"
                 f"  1. ?????????? ???????????????? --> {get_all(file)}\n"
                 f"  2. ???????????????????????? ?????????? ?????????? --> {get_max(file)}\n"
                 f"  3. ?????????????????????? ?????????? ?????????? --> {get_min(file)}\n"
                 f"  4. ?????????????? ?????????? ?????????? --> {get_sred(file)}\n"
                 f"  5. ???????????????????? ?????????????? --> {listr1[0]}\n"
                 f"  6. ???????????????????? ?????????????????? --> {listr1[1]}\n"
                 f"  7. ???????????????????? ???????????????????? ???????? ?? ???????????????????? ????????????:\n")


def get_analiz2(file):
    listr2 = get_sl(file)
    s: str = ""
    for i in range(1, len(listr2)):
        s += f"     * {i} ??????. >> {listr2[i]} ????????????.\n"
    return print(s)


def get_sl(file):
    sl1: int = 0
    sl2: int = 0
    sl3: int = 0
    sl4: int = 0
    sl5: int = 0
    sl6: int = 0
    sl7: int = 0
    sl8: int = 0
    sl9: int = 0
    sl10: int = 0
    with open(f'{file}', 'r') as file1:
        for line in file1.readlines():
            match len(line):
                case 1:
                    sl1 += 1
                case 2:
                    sl2 += 1
                case 3:
                    sl3 += 1
                case 4:
                    sl4 += 1
                case 5:
                    sl5 += 1
                case 6:
                    sl6 += 1
                case 7:
                    sl7 += 1
                case 8:
                    sl8 += 1
                case 9:
                    sl9 += 1
                case 10:
                    sl10 += 1
    return [sl1, sl2, sl3, sl4, sl5, sl6, sl6, sl7, sl8, sl9, sl10]

