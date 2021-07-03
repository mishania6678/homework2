words = input('Введите слова через пробел:').split()

for i in words:
    print(i if len(i) < 10 else i[:10])
