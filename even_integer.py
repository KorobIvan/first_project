from random import randint 



def even():
	"""function say even this digit or no
	return ansver and digit """
	digit = randint(1, 20) # Задаем число, четность которого будем определять
	if digit % 2 == 0: # если делится на 2 без остатка значит четоне
		ansver = 'Да' 
	else:
		ansver = 'Нет'
	return ansver, digit # выводим ответ и число

def even_results():
	"""add game vith even return""" 
	i = 0
	while i < 3: # игра до 3 очков 
		b, d = even() # присваиваем результатам предыдущей функции новые переменные
		user_ansver = input(f'Перед вами чесло: {d}\nНеобходимо ответить на вопрос, является данное число четным или нет (введите Да или Нет)?: ')
		if user_ansver == b:
			i += 1 
			print(f'Молодец!\nКоличество набранных очков = {i}')
		else:
			i = 0
			print(f'Попробуй еще раз!\nКоличество набранных очков = {i}')
		if i == 3:
			print('Поздравляю, вы успешно прошли мини-игру!!!')
if __name__ == '__main__':
    even_results()

