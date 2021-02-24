#Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
#Превратите строку "01/01/25 12:10:03.234567" в объект datetime

from datetime import datetime, timedelta, date

dt_today = datetime.now()
print(f'Сегодняшняя дата: {dt_today.strftime("%d.%m.%Y %H:%M")}')
delta = timedelta(days=1)
dt_yesterday = dt_today - delta
print(f'Вчерашнаяя дата: {dt_yesterday.strftime("%d.%m.%Y %H:%M")}')

date_string = "01/01/25 12:10:03.234567"
date_out = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
print(f'Превращенная строка в объект datetime, вжух: {date_out}')