from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    line1, line2, *_ = line.split('"')
    line1, line2 = line1.split(), line2.split()
    return line1[0], line2[0], line2[1]


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        list_out.append(get_parse_attrs(line))
pprint(list_out)
