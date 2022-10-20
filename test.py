symbols: list = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш',
                 'щ', 'b', 'l', 'm', 'n', 'd', 'q', 'k', 'p', 't', 'f', 'h', 'z', 'v', 'j']
sogl: int = 0
glasn: int = 0
stroka: str =""
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

try:
    file = open('f.txt', 'r')
    data = file.read()
    words = data.split()
    with open('f.txt', 'r') as file:
        for line in file.readlines():
            stroka += line
    with open('f.txt', 'r') as file:
        for line in file.readlines():
            match len(line):
                case 1:
                    sl1+=1
                case 2:
                    sl2+=1
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

    for sim in stroka:
        if sim in symbols:
            sogl += 1
        else:
            glasn += 1
    number = len(data)
    p = number / len(words)
    with open('f.txt', 'r') as file:
        min: str = min(file, key=len)
    with open('f.txt', 'r') as file:
        max = max(file, key=len)
    print(f"Всего символов:{number}\n"
          f"Максимальная длан слова:{len(max)}\n"
          f"Минимальная длина слова: {len(min)}\n "
          f"Количество слов:{len(words)}\n"
          f"Средняя длина слова:{p}\n"
          f"Количество согласных{sogl}\n"
          f"Количество гласных{glasn}\n"
          f"{sl1}\n{sl2}\n{sl3}\n{sl4}\n{sl5}\n{sl6}\n{sl7}\n{sl8}\n{sl9}\n{sl10}")

except Exception:
    pass
finally:
    file.close()
