# შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს

def get_info(info):
    return info * 3

get_info('word')




# შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას მთვარეზე

def weight_in_moon(weight):
    return weight // 6

weight_in_moon(54)




# შექმენი კალკულატორის ფუნქცია

number_1 = int(input('enter any number: '))
symbol = input('enter symbol: + - * / ^')
number_2 = int(input('enter any number: '))

def calculator(num_1, symb, num_2):
    if symb == '+':
        return f'{num_1} {symb} {num_2} = {num_1 + num_2}'
    elif symb == '-':
        return f'{num_1} {symb} {num_2} = {num_1 - num_2}'
    elif symb == '*':
        return f'{num_1} {symb} {num_2} = {num_1 * num_2}'
    elif symb == '/':
        if num_2 == 0:
            return "Division by zero is not allowed."
        return f'{num_1} {symb} {num_2} = {num_1 / num_2}'
    elif symb == '^':
        return f'{num_1} {symb} {num_2} = {num_1 ** num_2}'
    else:
        return "Invalid operator."

calculator(number_1, symbol, number_2)

