# -*- coding: utf-8 -*-
"""
Задание 7.1
Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

with open('ospf.txt', 'r') as f:
    for line in f:
        splitted_line = line.split()
        prefix = splitted_line[1]
        ad = splitted_line[2].strip('[]')
        next_hop = splitted_line[4].rstrip(',')
        last_upd = splitted_line[5].rstrip(',')
        interface = splitted_line[6]
        information = '''
            {:<20} {:<20}
            {:<20} {:<20}
            {:<20} {:<20}
            {:<20} {:<20}
            {:<20} {:<20}
           
        '''
        print(information.format('Prefix', prefix, 'AD/Metric', ad, 'Next-Hop', next_hop, 'Last update', last_upd, 'Outbound Interface', interface))