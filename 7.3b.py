# -*- coding: utf-8 -*-
"""
Задание 7.3b
Сделать копию скрипта задания 7.3a.
Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

vlan = input('Enter VLAN: ')
    
with open('CAM_table.txt', 'r') as f:
    for line in f:
        if 'DYNAMIC' in line:
            splitted_line = line.split()
            if splitted_line[0] == vlan:
                info = '''
                {:<10} {:<20} {:<6}
                '''
                print(info.format(vlan, splitted_line[1], splitted_line[3]))