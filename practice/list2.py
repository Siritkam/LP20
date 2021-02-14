List_new = [1, 2, 3, 4.1, "Python"]
print(f'Начальный элемент списка {List_new[0]}, а последний {List_new[-1]}')
print(f'Элементы списка со второго по четвертый включительно{List_new[2:5]}')
List_new.remove('Python')
print(f'Список с удаленным элементом Python {List_new}')