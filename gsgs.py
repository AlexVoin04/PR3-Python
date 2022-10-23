

def get_analiz2(file):
    listr2 = get_sl(file)
    s: str = ""
    print(listr2)
    for i in range(1, len(listr2)):
        s += f"   * {i} сим. >> {listr2[i]} повтор.\n"
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
    sl11: int = 0
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

filename = f"./result_files/Process-1-7356.txt"
get_analiz2(filename)