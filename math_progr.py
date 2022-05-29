from random import randint



def math_progrission(count_of_digit=7):
    """Add math progression
    return progression(string) and the searche namber""" 
    math_progression = '' #обнуляем будущую прогрессию                               
    first_digit = randint(1, 20)  # первое число прогресси задается в данном интервале 
    progrission_step = randint(1, 7)  # шаг прогрессии
    serche_digit_namder = randint(1, count_of_digit)  # выбираем какое именно число(по номеру) будет заменено на Х                                     
    for j in range(count_of_digit):  # цикл for в интревале от 0 до числа которое заложено в длину прогрессии
        current_digit = first_digit + progrission_step * j  # расчет текущего числа прогрессии
        if j+1 == serche_digit_namder:  # если шаг цикла + 1(т.к. цикл начинается с 0) численно равен переменной, которая отвечает за заменяемый номер позиции, то в прогрессию записываем Х вместо числа                
            math_progression += 'X '
            serche_digit = current_digit  # это число нам понадобится для сравнения с тем, которое ввел пользователь в выполнение программы
            #print(serche_digit)  # мне было лень считать каждый раз это чило 
        else:
            math_progression += f'{current_digit} '  # в прогрессию впичываем новое число
    return (math_progression, serche_digit)  # выводим кортеж из функции
def math_progrission_result():
    """Work with retern of math_progrission"""
    i = 0  # обнуляем счетчик итераций(очков набранных пользователем при прохождение игры)
    while i < 3:  # пользователь должен набрать 3 очка в этой игре
        text, z = math_progrission()  # распаковываем функцию                             
        print(f'Перед вами ряд чисел, допишите недостающее число:\n{text}')
        number = input('Введите пропущенное число: ') 
        try:  # проверка на ошибку, если вместо числа ввидут буквы или другие символы
            if int(number) == z:  # если число введенное пользователем совпадает с заменным на Х, тогда зарабатывает одно очко
                i += 1
                print('Великолепно, количество набранных очков: ',i)
            else:  # если не совпадает то сори твое очко уходит в зрительский зал и тебя ждет обнуление!!!!
                i = 0
                print('Попробуй еще раз, количество набранных очков: ',i)
        except ValueError:
            i = 0 
            print('Ошибка ввода, попробуй еще раз!')
if __name__ == '__main__':
    math_progrission_result()   
    
