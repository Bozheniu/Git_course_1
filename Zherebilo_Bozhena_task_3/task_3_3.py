

def thesaurus(*args) -> dict:
    input_dict = dict()
    for name in args:
        first_letter = name[0]
        if first_letter in input_dict:
            input_dict[first_letter].append(name)
        else:
            input_dict[first_letter] = [name]

    dict_out = dict()  # результирующий словарь значений
    for key in sorted(input_dict):
        dict_out[key] = input_dict[key]
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Эдуард", "Сергей", "Полина", "Светлана"))
