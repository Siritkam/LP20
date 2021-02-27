#Запишите содержимое списка словарей в файл в формате csv
import csv

names = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}
    ]

with open('mydictionary.csv', 'w', encoding='ansi') as myfile:
    fields_dict = ['name', 'age', 'job']
    writer = csv.DictWriter(myfile, fields_dict, delimiter=';')
    writer.writeheader()
    for members in names:
        writer.writerow(members)