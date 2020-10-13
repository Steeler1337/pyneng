# -*- coding: utf-8 -*-
"""
Задание 7.3a
Сделать копию скрипта задания 7.3.
Дополнить скрипт:
- Отсортировать вывод по номеру VLAN
В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9
Обратите внимание на vlan 1000 - он должен выводиться последним.
Правильной сортировки можно добиться, если vlan будет числом, а не строкой.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

vlans = []
sorted_vlans = []


sorted_distinct_vlans = []

with open('CAM_table.txt', 'r') as f:
    for line in f:
        if 'DYNAMIC' in line:
            splitted_line = line.split()
            vlans.append(int(splitted_line[0]))
    sorted_vlans = sorted(vlans)
print(sorted_vlans)


for i in range(len(sorted_vlans)):
    if sorted_vlans[i] not in sorted_distinct_vlans:
        sorted_distinct_vlans.append(sorted_vlans[i])
print(sorted_distinct_vlans)    

    
with open('CAM_table.txt', 'r') as f:
    for vlan in sorted_distinct_vlans:
        for line in f:
            if 'DYNAMIC' in line:
                splitted_line = line.split()
                if int(splitted_line[0]) == vlan:
                    info = '''
                    {:<10} {:<20} {:<6}
                    '''
                    print(info.format(vlan, splitted_line[1], splitted_line[3]))