def dict_solution():  # Через dict
    months = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
    for k, val in months.items():
        if month in val:
            return k


def list_solution():  # Через list
    months = [12, 'Зима', 1, 'Зима', 2, 'Зима', 3, 'Весна',  4, 'Весна',  5, 'Весна',
              6, 'Лето',  7, 'Лето',  8, 'Лето',  9, 'Осень',  10, 'Осень',  11, 'Осень']
    return months[months.index(month) + 1]


month = int(input('Введите порядковый номер месяца:'))
month_exist = True if 1 <= month <= 12 else False

# print(dict_solution()) if month_exist else print('Такого месяца не существует')
# print(list_solution()) if month_exist else print('Такого месяца не существует')
