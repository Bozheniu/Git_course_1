import os


def show_stat(check_dir):

    ramki = {10 ** x: 0 for x in range(1, 6)}
    ramki[0] = 0

    for item in os.walk(top=check_dir):
        files = item[2]
        if files:
            folder = item[0]
            for file in files:
                size = os.stat(os.path.join(folder, file)).st_size

                for key in sorted(ramki.keys()):
                    if size > key:
                        continue
                    else:
                        ramki[key] += 1
                        break

    return {ramki: value for ramki, value in sorted(ramki.items()) if value}


if __name__ == '__main__':
    check_dir = 'some_data'
    print(show_stat(check_dir))
