def given_number(input_number):
    i = 1
    while i <= 5:
        my_sum = input_number + i
        print(input_number, my_sum)
        i = i + 1
        if my_sum > 20:
            break

given_number(18)
