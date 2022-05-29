from ntpath import join
from random import randint


def prime_number():
    line = sorted(set(randint(1, 20) for i in range(15)))
    #print(line)
    z = ''
    for i in line:
        j = 0
        #print(i)
        for a in range(20):
            #print(a)
            if i % (int(a) + 1) == 0:
                j += 1
                #print(j)
        if j <= 2:
            z += f'{str(i)}, '
    return (line, z[:-2])

#print(prime_number())
def prime_number_result():
    """mini-game vith prime number, you need write prime number on line"""
    i = 0  # обнуляем счетчик итераций(очков набранных пользователем при прохождение игры)
    while i < 3:  # пользователь должен набрать 3 очка в этой игре
        line, z = prime_number()  # распаковываем функцию                            
        user_line = input(f'Перед вами ряд чисел: {(" ".join(map(str,line)))}\nЗапишите какие из них являются простыми, после каждого записаного числа ставьте запятую и пробел: ')
        try:
            if user_line == z:
                i += 1
                print(f'Молодец!\nКоличество набранных очков: {i}.')
            else: # если не совпадает, то обнуляется 
                i = 0
                print(f'Попробуй еще раз!\nКоличество набранных очков: {i}.')
        except ValueError: # блок работающий, когда вводишь текст вместо чисел
            i = 0 
            print('Ошибка ввода, попробуй еще раз!')
        if i == 3:
            print('Поздравляю, вы успешно прошли мини-игру!!!')
if __name__ == '__main__':
    prime_number_result()