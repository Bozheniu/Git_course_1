

def num_translate_adv(value):
    eng_rus_numbers = {
        "zero":'ноль',
        "one":'один',
        "two":'два',
        "three": 'три',
        "four": 'четыре',
        "five": 'пять',
        "six": 'шесть',
        "seven": 'семь',
        "eight": 'восемь',
        "nine": 'девять',
        "ten": 'десять'
    }
    word_lower = value.lower()
    if word_lower in eng_rus_numbers.keys():
        if 65 <= ord(value[0]) <= 90:
            return eng_rus_numbers[word_lower].title()
        return eng_rus_numbers[word_lower]


print(num_translate_adv("one"))
print(num_translate_adv("eight"))
print(num_translate_adv("Eight"))
