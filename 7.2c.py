from sys import argv
# -*- coding: utf-8 -*-
"""
Задание 7.2c
Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации
Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.
Проверить работу скрипта на примере файла config_sw1.txt.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

src = argv[1]
dest = argv[2]

ignore = ["duplex", "alias", "Current configuration"]


with open(src, 'r') as f, open(dest, 'w') as f1:
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