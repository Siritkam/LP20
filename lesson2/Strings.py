#Написать функцию, которая принимает на вход две строки
#Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
#Если строки одинаковые, вернуть 1
#Если строки разные и первая длиннее, вернуть 2
#Если строки разные и вторая строка 'learn', возвращает 3
#Вызвать функцию несколько раз, передавая ей разные параметры и выводя на экран результаты

string1 = input('Введите первую строку: ')
string2 = input('Введите вторую строку: ')

def string_chk (string1, string2):
    if string1 and string2 is type(str()):
        return(0)
    elif string1 == string2:
        return(1)
    elif string1 != string2 and len(string1) > len(string2):
        return(2)
    elif string1 != string2 and string2 == 'learn':
        return(3)
    else: return ('Ни одно условие не выполнено')

print(string_chk(string1, string2))