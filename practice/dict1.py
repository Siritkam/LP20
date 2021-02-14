Dict_new = {
    "city": "Moscow", 
    'temp': '20'
}
print(f'Выводим значение ключа city - {Dict_new["city"]}')
Dict_new["temp"] = 25
print(f'Выводим словарь, с измененным значением температуры {Dict_new}')

#Добавляем новый элемент в слоаврь
Dict_new['country'] = 'Россия'
Dict_new['date'] = '14.02.2021'
print(f'Выводим измененный словарь {Dict_new} и его длину ', len(Dict_new))