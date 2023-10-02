#первый тест
#print("    Три последовательных числа")
#first_number=int(input( 'введи первое число: '))
#print(first_number,first_number+1, first_number+2, sep='\n', end='\n')

#второй тест
#print('    Cумма трёх чисел')
#first_number=int(input( 'введи первое число: '))
#second_number=int(input( 'введи второе число: '))
#thrirt_number=int(input( 'введи третье число: '))
#print(first_number+second_number+thrirt_number)

#третий тест
#print('    Куб')
#first_number=int(input( 'введи что бы найти обьем и площадь: '))
#print('обьем: ',first_number**3)
#print('и площадь полной поверхности равен:', 6*first_number**2)

#четвертый тест
#print('    Значени функции')
#a=int(input( 'введи первое число: '))
#b=int(input( 'введи второе число: '))
#f= 3*(a + b)**3 + 275*b**2 - 127*a - 41
#print(f)

#пятый тест
#print('    Следующее и предыдущее')
#first_number=int(input( 'введи первое число: '))
#print('Cледующее за числом', first_number, str('число'), first_number+1)
#print('предыдущее за числом', first_number, str('число'), first_number-1)

#шестой тест
#print('     Стоимость покупки')
#monitor=int(input('стоимость монитора  '))
#sistem_unit=int(input('стоимость системного блока  '))
#keyboard=int(input('стоимость клавы  '))
#mause=int(input('стоимость мыши  '))
#print('три компа стоит: ', (monitor+sistem_unit+keyboard+mause)*3)

#седьмой тест
#print('    Арифметическая прогрессия')
#a_1=int(input('введите А1 арифметической прогрессии:  '))
#d=int(input('введите D арифметической прогрессии:  '))
#n=int(input('введите n арифметической прогрессии:  '))
#a_n=a_1+d*(n-1)
#print('A_n', str("равно"), a_n)

#восьмое задания
#print('     Разделяй и властвуй')
#first_number=int(input( 'введи число:  '))
#x=first_number
#print(x, x*2, x*3, x*4,x*5, sep='---')

#девятое задание
#print('     Мандарины')
#child=int(input('кол-во школьников:   '))
#mandarin=int(input('кол-во мандарин:   '))
#print('школьникам:  ', mandarin//child)
#print('в корзину:  ', mandarin%child)

#десятый тест
#print('     Сама неотвратимость')
#creature=int(input('колько всего существ?:   '))
#print(creature//2+creature%2)

#одинацатый тест
#print('     Пересчет временного интервала')
#interval=int(input('введите минуты чтоба перевести его и в часы:   '))
#print(interval, str('МИН -'), str('это'),interval//60, str('часа'), interval%60, str('минут'))

#двенадцатый
#print('      Трехзначное число')
#number = int(input("Введите трехзначное число: "))
#digit1 = number // 100
#digit2 = (number // 10) % 10
#digit3 = number % 10
#print("Сумма цифр:",digit1 + digit2 + digit3)
#print("Произведение цифр:", digit1 * digit2 * digit3)

#тринадцатый
#print('       Пингвины')
#n=int(input('кол-во пингвинов?:  '))
#print('        ~      '*n)
#print('       - -     '*n)
#print('     ( 0 0 )   '*n)
#print('    /   +   \  '*n)
#print('   /  ( - )  \ '*n)
#print('    ^^    ^^   '*n)

#14 тест
#print('        Вторая справа цифра')
#tenz=int(input('цифру:   '))
#n = (tenz // 10 ** 1) % 10
#print(n)

#15тест
#print('         Электронные часы')
#minutes=int(input(' минут прошло с начала дня:    '))
#days=minutes//60//24
#hours=minutes//60%24
#minute=minutes%60
#print('прошло',days , 'дня',hours ,'часов', minute,'минут')

#16 тест
#print('0 в 1 и наоборот')
#number=int(input('введи 1 или 0:   '))
#print(1-number%2)

#17 тест
#print('          Следующее четное')
#chet=int(input('след.чет:    '))
#print(chet+2-(chet%2))

#18 test
#print('МКАД')
#v=int(input('скорость:  '))
#time=int(input('час когда он остановился:  '))
#distance=v*time
#print(distance%109)


#19 test
#print('Улитка')
#h = int(input('высота:  '))
#a = int(input('поднимается:  '))
#b = int(input('спускатся:  '))
#print((h - a) // (a - b) + 1)
