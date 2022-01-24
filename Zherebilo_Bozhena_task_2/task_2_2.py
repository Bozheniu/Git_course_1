# Задание 2
'''a) Необходимо обработать список — обособить каждое целое число (вещественные не трогаем) кавычками
 (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём
 до двух целочисленных разрядов: '''

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
def convert_list_in_str(my_list: list) -> str:
    my_new_list = []
    for element in my_list:
        digit_list = element.isdigit()
        digit_list_symbols = (element[0] == "+" or element[0] == '-') and element[1:].isdigit()
        if digit_list or digit_list_symbols:
            if len(element) == 1:
                element = f'0{element}'
            elif digit_list_symbols and len(element[1:]) == 1:
                element = f'{element[0]}0{element[1:]}'
            my_new_list.append('"')
            my_new_list.append(element)
            my_new_list.append('"')
        else:
            my_new_list.append(element)
    str_out = my_new_list
    return str_out
print(convert_list_in_str(my_list))

'''b) Сформировать из обработанного списка строку:

в "05" часов "17" минут температура воздуха была "+05" градусов'''
new_list = ' '.join(convert_list_in_str(my_list))
print(new_list)




