from sys import argv

len_argv = len(argv)
with open("bakery.csv", 'r', encoding="UTF-8") as file:
    if len_argv == 1:
        print("Все записи цен:")
        for line in file:
            print(line.strip())
    elif len_argv == 2:
        record_begin = int(argv[1])
        print(f"Цены, начиная с {record_begin}:")
        for idx, line in enumerate(file):
            if idx >= record_begin-1:
                print(line.strip())
    else:
        record_begin = int(argv[1])
        record_end = int(argv[2])

        print(f"Цены, начиная с {record_begin}:")
        for idx, line in enumerate(file):
            if record_begin-1 <= idx <= record_end-1:
                print(line.strip())