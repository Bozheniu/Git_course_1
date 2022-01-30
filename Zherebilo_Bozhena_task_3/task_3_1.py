

def num_translate(value: str) -> str:
    eng_rus_numbers = {
        "zero": 'ноль',
        "one": 'один',
        "two": 'два',
        "three": 'три',
        "four": 'четыре',
        "five": 'пять',
        "six": 'шесть',
        "seven": 'семь',
        "eight": 'восемь',
        "nine": 'девять',
        "ten": 'десять'
    }
    str_out = eng_rus_numbers.get(value)
    return str_out


print(num_translate("one"))
print(num_translate("eight"))
print(num_translate("seventeen"))

