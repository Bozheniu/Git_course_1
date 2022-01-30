nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

import random

list_out = []


def get_jokes(count: int) -> list:
    for i in range(count):
        joke_list = list(map(random.choice, [nouns, adverbs, adjectives]))
        list_out.append(' '.join(joke_list))
    return list_out


print(get_jokes(2))
print(get_jokes(8))