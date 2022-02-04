
def get_numbers(src: list):
    lst = [src[idx] for idx in range(2, len(src)) if src[idx] > src[idx - 1]]
    yield lst

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))

