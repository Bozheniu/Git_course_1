def get_uniq_numbers(src: list):
    unique = set()
    not_unique = set()
    for el in src:
        if el not in not_unique:
            unique.add(el)
        else:
            unique.discard(el)
        not_unique.add(el)
    unique_list = [el for el in src if el in unique]
    return unique_list


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))