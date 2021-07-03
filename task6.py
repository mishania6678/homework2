try:
    products = {
        'название': input('Введите названия товаров через пробел:').split(),
        'цена': list(map(int, input('Введите цену введенных товаров через пробел:').split())),
        'кол-во': list(map(int, input('Введите кол-во введенных товаров через пробел:').split())),
        'ед.': input('Введите единицу измерения товаров:')
    }

    # Например, переводим "шт." в "шт. * кол-во товаров", чтоб возможно было все значения зипнуть
    products['ед.'] = ((products['ед.'] + ' ') * len(products['название'])).split()

    lst = []
    for i in range(1, len(products['название']) + 1):
        # Зипаем ключи с зипнутыми значениями и переводим все в словарь
        lst.append((i, dict(zip(products.keys(), list(zip(*products.values()))[i - 1]))))

    for i in lst:
        print(i)

except Exception:
    print('Некорректный формат входных данных')

# test1
