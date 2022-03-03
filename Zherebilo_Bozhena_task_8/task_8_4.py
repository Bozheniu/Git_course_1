from functools import wraps


def val_checker(func):
    def val_checker_1(func_1):
        @wraps(func_1)
        def wrapper(*args):
            if args:
                for arg in args:
                    if not func(arg):
                        raise ValueError(f'wrong val {arg}')
            return func_1(*args)
        return wrapper
    return val_checker_1


def validator(i):
    if isinstance(i, int) and i >= 0:
        return True
    return False


@val_checker(validator)
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))
