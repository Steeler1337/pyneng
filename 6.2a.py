# -*- coding: utf-8 -*-
"""
Задание 6.2a
Сделать копию скрипта задания 6.2.
Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255
Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'
Сообщение должно выводиться только один раз.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Enter an ip address: ')
oktets = ip.split('.')
try:
    check = int(oktets[0])
    check = int(oktets[1])
    check = int(oktets[2])
    check = int(oktets[3])
    if len(oktets) == 4 and int(oktets[0]) >= 0 and int(oktets[0]) <=255 and int(oktets[1]) >= 0 and int(oktets[1]) <=255 and int(oktets[2]) >= 0 and int(oktets[2]) <=255 and int(oktets[3]) >= 0 and int(oktets[3]) <=255:
        if int(oktets[0]) >= 1 and int(oktets[0]) <= 223:
            print('\nunicast')
        elif int(oktets[0]) >= 224 and int(oktets[0]) <= 239:
            print('\nmulticast')
        elif ip == '255.255.255.255':
            print('\nlocal broadcast')
        elif ip == '0.0.0.0':
            print('\nunassigned')
        else: 
            print('\nunused')
    else:
        print('\nIncorrect ip-address1')
except ValueError:
    print('\nIncorrect ip-address2')


    









