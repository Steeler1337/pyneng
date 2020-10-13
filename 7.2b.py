from sys import argv
# -*- coding: utf-8 -*-
"""
Задание 7.2b
Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt
При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]



name_program = argv[1]

with open(name_program, 'r') as f, open('config_sw1_cleared.txt', 'w') as f1:
    for line in f:
        #if line.startswith('!'):
            #continue
        #elif 
        if not line:
            continue
        elif ignore[0] in line or ignore[1] in line or ignore[2] in line:
            continue
        else:
            f1.write(line)