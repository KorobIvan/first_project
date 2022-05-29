import math_progr
import calculator
import join_division
import prime_number

name = input('Введите ваше имя: ')
print(f'Привет, {name}!\nТебе нужно пройти математическую игру.\nОна состоит из 4 мини игр, если ты даешь правильный ответ, то получаешь один балл, если не правильный теряешь набранные.\nКогда вы наберете 3 очка, то сможете приступить к следующей мини игре!\nУдачи!')
calculator.calculate_line_result()
print('Молодец, приступай к следующей мини-игре!\n')
math_progr.math_progrission_result()
print('Молодец, приступай к следующей мини-игре!\n')
join_division.division_result()
print('Молодец, приступай к следующей мини-игре!\n')
prime_number.prime_number_result()
print('Замечательно, вы прошли игру, возьми с полки пирожок, ты его заслужил!!!!')