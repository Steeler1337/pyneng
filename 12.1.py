# -*- coding: utf-8 -*-
import subprocess
"""
Задание 12.1
Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Функция ожидает как аргумент список IP-адресов.
Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов
Для проверки доступности IP-адреса, используйте команду ping.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

addresses=['87.250.250.242', 'a', '173.194.222.113']


def ping_ip_addresses(list_of_addresses):
    working_addresses = []
    not_working_adresses = []
    for address in list_of_addresses:
        reply = subprocess.run(['ping', address],stdout = subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if reply.returncode == 0:
            working_addresses.append(address)
        else:
            not_working_adresses.append(address)
    my_tuple = (working_addresses, not_working_adresses)
    return my_tuple
    
print(ping_ip_addresses(addresses))