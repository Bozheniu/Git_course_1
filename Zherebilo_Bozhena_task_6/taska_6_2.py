noise_surfing = {}
with open("nginx_logs.txt", 'r', encoding="UTF-8") as fr:
    for line in fr:
        line1, *_ = line.split('"')
        address = line1.split()[0]
        if address not in noise_surfing.keys():
            noise_surfing[address] = 1
        else:
            noise_surfing[address] += 1

spam = max(noise_surfing.values())
for key, val in noise_surfing.items():
    if val == spam:
        print(f'Адрес спамера: {key}, Количество отправленных им запросов: {val}')
