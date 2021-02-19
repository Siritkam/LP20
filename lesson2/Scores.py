# Создать список из словарей с оценками учеников разных классов школы 
# вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

classes = [
    {'school_class': '1a', 'scores': [5, 5, 4, 5, 3]},
    {'school_class': '1b', 'scores': [2, 4, 3, 3, 3]},
    {'school_class': '1c', 'scores': [5, 5, 5, 5, 5]},
    {'school_class': '1d', 'scores': [5, 5, 3, 3, 3]},
    {'school_class': '1e', 'scores': [4, 4, 4, 5, 3]}
]
print
print('Средний бал в каждом классе: ')
for score_cls in classes:
    print((sum(score_cls["scores"])) / (len(score_cls["scores"])))

