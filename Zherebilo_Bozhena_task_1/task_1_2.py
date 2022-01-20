sum_numbers = 0
indx = 1
while indx <= 1000:
    number = indx ** 3
    number_result = number
    sum_digit = 0
    while True:
        sum_digit += number_result % 10
        number_result //= 10
        if number_result == 0:
            break
    if sum_digit % 7 == 0:
        sum_numbers += indx
        print(indx, '^3 :', number, 'sum:', sum_numbers, sum_digit)
    indx += 2





