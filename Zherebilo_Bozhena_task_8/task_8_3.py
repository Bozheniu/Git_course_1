from functools import wraps


def type_logger(calc_cube):
    @wraps(calc_cube)
    def wrapper(*args):
        #result = calc_cube(*args)
        #print(result)
        for i in range(len(args)):
            if i < len(args) - 1:
                print(f'{calc_cube.__name__} {args[i]}: {type(args[i])}')
            elif i == len(args) - 1:
                print(f'{calc_cube.__name__} {args[i]}: {type(args[i])}')
        #return result
    return wrapper


@type_logger
def calc_cube(x):
   return x ** 3


#calc_cube(5)
calc_cube(5, 6, 7)
