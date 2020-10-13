# -*- coding: utf-8 -*-
"""
Задание 5.3a
Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'
Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

mode = input('Enter a mode (access/trunk): ')
interface = input('Enter type and number of the interface: ')
if mode == 'access':
    vlan = input('Enter vlan number(s): ')
elif mode == 'trunk':
    vlan = input('Enter allowed vlan number(s): ')



print('\n' + '-' * 30)
print('interface {}'.format(interface))

if mode == 'access':
    print('\n'.join(access_template).format(vlan))
elif mode =='trunk':
    print('\n'.join(trunk_template).format(vlan))