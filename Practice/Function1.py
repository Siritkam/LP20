#Задание 1 по теме функции
def get_summ(one, two, delimiter='&'):
    a = one + delimiter + two
    print(a.upper())

get_summ('Learn', 'python')