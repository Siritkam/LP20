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