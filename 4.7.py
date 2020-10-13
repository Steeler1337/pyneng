# -*- coding: utf-8 -*-
"""
Задание 4.7
Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


mac = "AAAA:BBBB:CCCC"

mac_lower = mac.lower()
splitted = mac_lower.split(':')

digit = list(splitted[0])
row = ''
row += '{:b}{:b}{:b}{:b}'.format(int(digit[0], 16), int(digit[1], 16), int(digit[2], 16), int(digit[3], 16))
digit = list(splitted[1])
row += '{:b}{:b}{:b}{:b}'.format(int(digit[0], 16), int(digit[1], 16), int(digit[2], 16), int(digit[3], 16))
digit = list(splitted[2])
row += '{:b}{:b}{:b}{:b}'.format(int(digit[0], 16), int(digit[1], 16), int(digit[2], 16), int(digit[3], 16))
print(row)