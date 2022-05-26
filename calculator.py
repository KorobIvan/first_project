from random import randint


def calculate_line():
    """add line for calculator
    return line and search digit"""
    list_of_characters = '+-/*' # ряд символов для действия
    index_of_simbol = randint(0,3) # выбор случайного числа от 0 до 3
    first_digit = randint(10,20) # выбор случайного числа 10 до 20 это первое число в действие
    second_digit = randint(1,10) # выбор случайного числа 1 до 10 это второе число в действие
    simbol_of_calculate = list_of_characters[index_of_simbol] # выбор случайного символа из ряда возможных
    if simbol_of_calculate == '+': # дальше идут перечисления действий при выпадение того ли иного символа
        search_digit = first_digit + second_digit
    elif simbol_of_calculate == '-':
        search_digit = first_digit - second_digit
    elif simbol_of_calculate == '/':
        search_digit = first_digit // second_digit
    elif simbol_of_calculate == '*':
        search_digit = first_digit * second_digit
    line = f'{first_digit} {simbol_of_calculate} {second_digit}'
    return line, search_digit
def calculate_line_result():
    """add game vith calculate line results"""
    i = 0
    while i < 3:
        a, b = calculate_line() # присваиваю внешним переменным значения из функции 
        print(a, b)
        number = input('Введите результат действия (при /, округлите число до целого): ') # вводим правильный ответ 
        try: # исключение ошибки с введением текста вместо числа 
            if int(number) == b: # проверка правильности введенного числа 
                i += 1
                print(f'Молодец!\nКоличество набранных очков = {i}')
            else:
                i = 0
                print(f'Попробуй еще раз!\nКоличество набранных очков = {i}')
        except ValueError:
            i = 0 
            print('Ошибка ввода, попробуй еще раз!')
        if i == 3:
            print('Поздравляю, вы успешно прошли мини-игру!!!')
if __name__ == '__main__':
    calculate_line_result()