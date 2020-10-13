# -*- coding: utf-8 -*-
"""
Задание 4.5
Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).
Результатом должен быть такой список: ['1', '3', '8']
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

splitted_command1 = command1.split()
vlan1 = splitted_command1[-1].split(',')
vlan1_set = set(vlan1)
splitted_command2 = command2.split()
vlan2 = splitted_command2[-1].split(',')
vlan2_set = set(vlan2)
vlans_list = list(vlan1_set.intersection(vlan2_set))
print(sorted(vlans_list))