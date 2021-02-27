#Прочитайте содержимое файла в переменную, 
#подсчитайте длину получившейся строки
#Подсчитайте количество слов в тексте
#Замените точки в тексте на восклицательные знаки
#Сохраните результат в файл referat2.txt

with open('referat.txt', 'r', encoding='utf-8') as read_f:
    content = read_f.read()
    print(f'Длина получившейся строки составляет: {len(content)} символов')
with open('referat.txt', 'r', encoding='utf-8') as read_f:
    words = len(read_f.read().split())
    print(f'Количество слов в тексте равно: {words}')
with open('referat.txt', 'r', encoding='utf-8') as read_f:
    for dots in read_f:
        dots = read_f.read()
        with open('referat2.txt', 'w', encoding='utf-8') as ref2:
            ref2.write(dots.replace('.', '!'))
