from random import*

#создание ответа компьютера
otvet1 = randint(1,3)

#создание ответа пользователя    
otvet2 = input('введи свой ответ(бумага,ножницы,камень):')

#проверка ответов игрока
if otvet2== 'бумага':
    print('бумага')
elif otvet2== 'ножницы':
    print('ножницы')
elif otvet2== 'камень':
    print('камень')

#проверка ответов компьютера
if otvet1== 1:
    print('бумага')
elif otvet1== 2:
    print('ножницы')
elif otvet1== 3:
    print('камень')

#процесс выбора победителя
if otvet1== 1 and otvet2== 'ножницы':
    print('Пользователь одержал победу')
elif otvet1== 1 and otvet2== 'камень':
    print('Компьютер одержал победу')
    
elif otvet1== 2 and otvet2== 'бумага':
    print('Компьютер одержал победу')
elif otvet1== 2 and otvet2== 'камень':
    print('Пользователь одержал победу')
    
elif otvet1== 3 and otvet2== 'бумага':
    print('Пользователь одержал победу')
elif otvet1== 3 and otvet2== 'ножницы':
    print('Компьютер одержал победу')
else:
    print('Ничья')
