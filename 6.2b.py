# -*- coding: utf-8 -*-
"""
Задание 6.2b
Сделать копию скрипта задания 6.2a.
Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Enter an ip address: ')
oktets = ip.split('.')

address_correct = False

while not address_correct:
    if len(oktets) != 4:
        print('\nIncorrect address!')
        ip = input('Enter an ip address again: ')
        oktets = ip.split('.')
    elif int(oktets[0]) < 0 and int(oktets[0]) > 255 and int(oktets[1]) < 0 and int(oktets[1]) > 255 and int(oktets[2]) < 0 and int(oktets[2]) > 255 and int(oktets[3]) < 0 and int(oktets[3]) > 255:
        print('\nIncorrect address!')
        ip = input('Enter an ip address again: ')
        oktets = ip.split('.')
    else:
        try:
            check = int(oktets[0])
            check = int(oktets[1])
            check = int(oktets[2])
            check = int(oktets[3])
            
            if int(oktets[0]) >= 1 and int(oktets[0]) <= 223:
                print('\nunicast')
                address_correct = True
            elif int(oktets[0]) >= 224 and int(oktets[0]) <= 239:
                print('\nmulticast')
                address_correct = True
            elif ip == '255.255.255.255':
                print('\nlocal broadcast')
                address_correct = True
            elif ip == '0.0.0.0':
                print('\nunassigned')
                address_correct = True
            else: 
                print('\nunused')
                address_correct = True
        except ValueError:
            print('\nIncorrect address!')
            ip = input('Enter an ip address again: ')
            oktets = ip.split('.')