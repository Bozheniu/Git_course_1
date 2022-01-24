# Задание 4

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

def convert_name_extract( my_list: list) -> list:
    for element in my_list:
        element = element.split()
        staff_name = element[-1].title()
        list_out = f'Привет, {staff_name}!'
        print(f'Привет, {staff_name}!')
    return list_out


result = convert_name_extract(my_list)
print(result)
