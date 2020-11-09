# -*- coding: utf-8 -*-
"""
Задание 9.3
Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}
* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}
У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.
Проверить работу функции на примере файла config_sw1.txt
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(file_name):
    final_tuple = ''
    with open(file_name, 'r') as f:
        name_interface = ''
        configuration_access = {}
        configuration_trunk = {}
        for line in f:           
            if line.startswith('interface Fast'):
                name_interface = line.split()[1]
            if 'access vlan' in line:
                vlan_number = int(line.split()[3])
                configuration_access[name_interface] = vlan_number
                name_interface = ''
            elif 'allowed vlan' in line:              
                vlan_number = line.split()[4].split(',')
                vlan_digit = []
                for item in vlan_number:
                    vlan_digit.append(int(item))
                configuration_trunk[name_interface] = vlan_digit
                name_interface = ''
        final_tuple = tuple((configuration_access, configuration_trunk))
    return final_tuple
                
result = get_int_vlan_map('config_sw1.txt')
print(result)

