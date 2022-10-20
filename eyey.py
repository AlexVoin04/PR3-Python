symbols :list = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч','ш', 'щ', 'b', 'l', 'm','n','d','q', 'k', 'p','t','f','h','z','v','j']

sogl: int = 0
glasn: int = 0
file = open('f.txt', 'r')
data = file.read()
words = data.split()
min = min(file, key=len)
for slovo in file:
        for sim in slovo:
                if sim in symbols:
                        sogl += 1
                else:
                        glasn += 1
number = len(data)
p = number/len(words)
with open('f.txt', 'r') as file:
        min = min(file, key=len)
with open('f.txt', 'r') as file:
        max = max(file, key=len)
file.close()
print(f"{number}\n{len(max)}\n{len(min)}\n{len(words)}\n{p}\n{sogl}\n{glasn}")