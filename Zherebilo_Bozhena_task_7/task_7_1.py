import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
my_starter = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}


def making_dir(base_dir, starter):
    for key, val in starter.items():
        folder = os.path.join(base_dir, key)
        if not os.path.exists(folder):
            os.mkdir(folder)
        for el in val:
            folder = os.path.join(base_dir, key, el)
            if not os.path.exists(folder):
                os.mkdir(folder)


if __name__ == '__main__':
    making_dir(BASE_DIR, my_starter)
