def add_three_numbers(num1, num2, num3=0):
    def print_number(num):
        print(f'The number is {num}')
    print_number(num1)
    print_number(num2)
    print_number(num3)

def add_three_numbers(num1, num2):
    print('Do nothing')

x = add_three_numbers(7, 8)
print(x)

