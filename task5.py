lst = [7, 5, 3, 3, 2]
print(f'Текущий рейтинг: {" ".join(list(map(str, lst)))}')

while True:
    new_item = input('Введите новый елемент рейтинга (q - выход):')

    if new_item == 'q':
        print('Выход из программы...')
        break

    if not new_item.isdigit():
        print('Вы ввели не число')
    else:
        lst.append(int(new_item))
        lst = sorted(lst, reverse=True)
        print(f'Новый рейтинг: {" ".join(list(map(str, lst)))}')

# test2
