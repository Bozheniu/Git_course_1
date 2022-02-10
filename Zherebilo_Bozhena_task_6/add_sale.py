from sys import argv

if len(argv) < 2:
    print("Сумма продаж не передана")
    exit(1)

with open('bakery.csv', 'a', encoding="UTF-8") as f:
    f.write(f'{argv[1]}\n')