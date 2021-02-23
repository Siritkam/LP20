#Перепишите функцию discounted(price, discount, max_discount=20) из урока про функции так, 
#чтобы она перехватывала исключения, когда переданы некорректные аргументы.

#Первые два нужно приводить к вещественному числу при помощи float(), 
#а третий - к целому при помощи int() и перехватывать исключения ValueError и TypeError, 
#если приведение типов не сработало.

def discounted(price, discount, max_discount=50):
    try:
        price = abs(price)
        discount = abs(discount)
        max_discount = abs(max_discount)
        
        if max_discount > 99:
            raise ValueError('Максимальная скидка не может быть больше 99%')
    
        if discount >= max_discount:
            price_with_discount = price
        else:
            price_with_discount = price - price * discount / 100
            return price_with_discount
    except (ValueError, TypeError):
        print('Введены не верные значения')


print(discounted(100, '2'))