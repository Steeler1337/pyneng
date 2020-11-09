# -*- coding: utf-8 -*-
"""
Задание 9.3a
Сделать копию функции get_int_vlan_map из задания 9.3.
Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1
В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }
У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.
Проверить работу функции на примере файла config_sw2.txt
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""



def get_int_vlan_map(file_name):
    final_tuple = ''
    checker = 0;
    with open(file_name, 'r') as f:
        name_interface = ''
        configuration_access = {}
        configuration_trunk = {}
        for line in f:
            if line.startswith('interface Fast'):
                name_interface = line.split()[1]
            if checker == 2:
                configuration_access[name_interface] = 1
                checker = 0
            if 'switchport mode access' in line:
                checker += 1
            if 'duplex auto' in line:
                checker += 1
            if 'access vlan' in line:
                vlan_number = int(line.split()[3])
                configuration_access[name_interface] = vlan_number
                name_interface = ''
                checker = 0
            elif 'allowed vlan' in line:              
                vlan_number = line.split()[4].split(',')
                vlan_digit = []
                for item in vlan_number:
                    vlan_digit.append(int(item))
                configuration_trunk[name_interface] = vlan_digit
                name_interface = ''
                checker = 0
            
        
        final_tuple = tuple((configuration_access, configuration_trunk))
    return final_tuple
                
result = get_int_vlan_map('config_sw2.txt')
print(result)