duration = int(input('Введите время в секундах:\n'))
if 0 <= duration < 60:
    print(str(duration), 'сек')
elif 60 <= duration < 3600:
    minutes = duration//60
    seconds = duration % 60
    print(str(minutes), 'мин', str(seconds), 'сек')
elif 3600 <= duration < 86400:
    hours = duration//3600
    duration1 = duration - hours*3600
    minutes = duration1//60
    seconds = duration1 % 60
    print(str(hours), 'час', str(minutes), 'мин', str(seconds), 'сек')
else:
    days = duration//86400
    duration2 = duration - days*86400
    hours = duration2//3600
    duration3 = duration2 - hours*3600
    minutes = duration3//60
    seconds = duration3 % 60
    print(str(days), 'дн', str(hours), 'час', str(minutes), 'мин', str(seconds), 'сек')
