import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    users_list = []
    with open(path_users_file, 'r', encoding='utf-8') as fr:
        for line in fr:
            users_list.append(line.replace(',', ' ').strip())

    hobby_list = []
    with open(path_hobby_file, 'r', encoding='utf-8') as fr:
        for line in fr:
            hobby_list.append(line.strip())
    user_dict = {}
    if len(users_list) >= len(hobby_list):
        while len(users_list) > len(hobby_list):
            hobby_list.append(None)
        counter = 0
        for name in users_list:
            user_dict[name] = hobby_list[counter]
            counter += 1
    else:
        user_dict = sys.exit(1)
    return user_dict


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
