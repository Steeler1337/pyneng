# -*- coding: utf-8 -*-
"""
Задание 5.2a
Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.
Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16
Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28
Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:
Network:
10        0         1         0
00001010  00000000  00000001  00000000
Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24
Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28  в двоичном формате будет
bin_ip = "00001010000000010000000111000011"
А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

#10.1.1.195/28

address_string = input('Enter an IP network address: ')

ip = address_string[0:address_string.find('/')]
ip_splitted = ip.split('.')

bin_ip_full = ''

bin_ip_0b = bin(int(ip_splitted[0]))
bin_ip = bin_ip_0b[2::]
bin_ip_full = bin_ip_full + '0' * (8 - len(bin_ip)) + bin_ip
bin_ip_0b = bin(int(ip_splitted[1]))
bin_ip = bin_ip_0b[2::]
bin_ip_full =  bin_ip_full + '0' * (8 - len(bin_ip)) + bin_ip
bin_ip_0b = bin(int(ip_splitted[2]))
bin_ip = bin_ip_0b[2::]
bin_ip_full =  bin_ip_full + '0' * (8 - len(bin_ip)) + bin_ip
bin_ip_0b = bin(int(ip_splitted[3]))
bin_ip = bin_ip_0b[2::]
bin_ip_full = bin_ip_full + '0' * (8 - len(bin_ip)) + bin_ip

mask = address_string[address_string.find('/') + 1:]
bin_ip_full_net = bin_ip_full[0 : int(mask)] + '0' * (32 - int(mask))

ip_splitted[3]  = int(bin_ip_full_net[24:32], 2)
#print('Последний октет: ' + str(ip_splitted[3]))


#print('Хост: ' + bin_ip_full)
#print('Сеть: ' + bin_ip_full_net)



print('\nNetwork:')
information = '''
    {0:<8} {1:<8} {2:<8} {3:<8}
    {0:08b} {1:08b} {2:08b} {3:08b}
    '''
print(information.format(int(ip_splitted[0]), int(ip_splitted[1]), int(ip_splitted[2]), int(ip_splitted[3])))

mask2 = address_string[address_string.find('/'):]
print('\nMask:')
print(mask2)
mask_number = mask2[1:]
binary_mask = '1' * int(mask_number) + '0' * (32 - int(mask_number))
first_okt_mask = binary_mask[0:8]
first_okt_number = int(first_okt_mask, 2)
second_okt_mask = binary_mask[8:16]
second_okt_number = int(second_okt_mask, 2)
third_okt_mask = binary_mask[16:24]
third_okt_number = int(third_okt_mask, 2)
fourth_okt_mask = binary_mask[24:32]
fourth_okt_number = int(fourth_okt_mask, 2)

information2 = '''
    {0:<8} {1:<8} {2:<8} {3:<8}
    {4:<8} {5:<8} {6:<8} {7:<8}
'''
print(information2.format(first_okt_number, second_okt_number, third_okt_number, fourth_okt_number, first_okt_mask, second_okt_mask, third_okt_mask, fourth_okt_mask))



