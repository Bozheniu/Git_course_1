from random import uniform
my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
def transfer_list_in_str(my_list: list) -> str:
    for cost in my_list:
        cost_rub = int(cost)
        cost_coin = round((cost - cost_rub)*100)
        str_out = f'{cost_rub} руб {cost_coin:02d} коп'
        print(str_out, end=", ")
    return str_out
result_1 = transfer_list_in_str(my_list)
print(result_1)


print("\nДоказательство операции in place:")
print(f"id перед сортировкой {id(my_list)}")
my_list.sort()

print(f"id после сортировки {id(my_list)}")

my_list_descending = list(reversed(my_list))
print("5 самых дорогих товаров:")
for cost in my_list_descending[:5]:
    print(f"{cost}")