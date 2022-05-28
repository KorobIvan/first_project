from random import randint
from functools import reduce


def division():
    """add 2 digit and max division digit of this digit
    retern digit_1 and digit_2 and max_division_digit"""
    digit_1 = randint(1,20) # Задаем рандомное число в интервале 
    digit_2 = randint(1,20) # Задаем рандомное число в интервале
    max_division_digit = 0
    for i in range(1, reduce(min, [digit_1, digit_2]) + 1): # наченаем перебиравть все числа от 1 до самого маленького из первых 2 чисел
        if digit_1 % i == 0 and digit_2 % i == 0: # если первое и второе число делятся на число которое перебирают, то нужно запомнить его 
            max_division_digit = i # кода находится число которое делится и на первое и на второе число без остатка, то оно записывается в пременную
    return (digit_1, digit_2, max_division_digit)

def division_result():
    """mini-game vith division, you need say max division digit """
    j = 0
    while j < 3: # игра продолжается до 3 набранных очков
        a, b, c = division() # присвоение вызываемым из функции аргументам новых имен
        result = input(f'Перед вами два числа: {a}, {b}.\nНеобходимо написать наибольший общий делитель: ') # Выводится 2 числа, пишем наибольший общий делитель
        try: # исключение ошибки введения текста 
            if int(result) == c: # если введенное число совпадает с вычесленным числом то счетчик очков увеличивается 
                j += 1
                print(f'Молодец!\nКоличество набранных очков: {j}.')
            else: # если не совпадает, то обнуляется 
                j = 0
                print(f'Попробуй еще раз!\nКоличество набранных очков: {j}.')
        except ValueError: # блок работающий, когда вводишь текст вместо чисел
            j = 0 
            print('Ошибка ввода, попробуй еще раз!')
        if j == 3:
            print('Поздравляю, вы успешно прошли мини-игру!!!')
if __name__ == '__main__': # блок импортирования
    division_result()