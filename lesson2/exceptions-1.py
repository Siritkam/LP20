#Перепишите функцию hello_user() из задания про while, 
#чтобы она перехватывала KeyboardInterrupt, писала пользователю "Пока!"
#и завершала работу при помощи оператора break

def hello_user():
    while True:
        try:
            user_say = input('Как дела? ')
            if user_say in ['хорошо', 'Хорошо']:
                print('Ну пока')
        except KeyboardInterrupt:
            print('ПОКА')
            break
    else:
        print('ну и ладно')


hello_user()