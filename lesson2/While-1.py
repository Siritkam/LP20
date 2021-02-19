#Напишите функцию hello_user(), которая с помощью функции input() 
#спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”

def hello_user():
    while True:
        user_say = input('Как дела? ')
        if user_say in ['хорошо', 'Хорошо']:
            print('Ну пока')
            break
    else:
        print('ну и ладно')


hello_user()