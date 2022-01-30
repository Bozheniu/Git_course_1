

def thesaurus_adv(*args) -> dict:
    input_dict = dict()
    for person in args:
        name, surname = person.split()
        first_letter_name = name[0]
        first_letter_surname = surname[0]
        if first_letter_surname not in input_dict.keys(): #создаю словарь для буквы-фамилии, которая встречается впервые
            input_dict[first_letter_surname] = {}
        if first_letter_name not in input_dict[first_letter_surname].keys(): #создаю список для буквы-имени, которая встречается впервые
            input_dict[first_letter_surname][first_letter_name] = []
        input_dict[first_letter_surname][first_letter_name].append(person)
    sort_dict = dict() #сортирую по буква-фамилии и буква-имени
    for surname in sorted(input_dict.keys()):
        sort_dict[surname]={}
        for name in sorted(input_dict[surname].keys()):
            sort_dict[surname][name] = input_dict[surname][name]
    return sort_dict


persons = ["Иван Сергеев", "Божена Жеребило", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]

dict_out = thesaurus_adv(*persons)
for person_surname in dict_out.keys():
    print(person_surname, ":")
    for person_name in dict_out[person_surname].keys():
        print(f"\t{person_name}: {dict_out[person_surname][person_name]}")
