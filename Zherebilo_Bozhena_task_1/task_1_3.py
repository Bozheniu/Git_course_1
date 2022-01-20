def transform_string (element):
    if element == 0:
        return f'{element} процентов'
    elif 11 <= element <= 14:
        return f'{element} процентов'
    if element % 10 == 1:
        return f'{element} процент'
    if 2 <= element <= 4:
        return f'{element} процента'
    if 1 <= element % 10 <= 4:
        return f'{element} процента'
    else:
        return f'{element} процентов'
n = 101
for i in range(1, n):
    print(transform_string(i))
