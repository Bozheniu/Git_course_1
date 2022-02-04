tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Александра', 'Володя']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    length = len(klasses)
    for idx, person in enumerate(tutors):
        if idx < length:
            yield tutors[idx], klasses[idx]
        else:
            yield person, None


generator = check_gen(tutors, klasses)
# добавьте здесь доказательство, что создали именно генератор
print(f'Тип нашего объекта: {type(generator)}')

for _ in range(len(tutors)):
    print(next(generator))