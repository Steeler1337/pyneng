# -*- coding: utf-8 -*-
"""
Задание 12.2
Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.
В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.
Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.
Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10
Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.
Функция возвращает список IP-адресов.
Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']
"""


ips = ['12.31.5.1', '10.1.1.1-10.1.1.10', '255.255.255.255', '1.1.1.1-3', '1.1.1.20-25', '175.75.43.50-175.75.43.55']


def convert_ranges_to_ip_list(list_of_addresses):
    distinct_addresses = []
    for address in list_of_addresses:
        split_checker = address.split('.')
        if '-' in split_checker[3] and len(split_checker) > 4:
            splitted_address = address.split('-')
            oktets_of_minuend = splitted_address[1].split('.')
            minuend = int(oktets_of_minuend[-1])
            oktets_of_subtrahend = splitted_address[0].split('.')
            subtrahend = int(oktets_of_subtrahend[-1])
            ready_address = str(splitted_address[0])
            distinct_addresses.append(ready_address)
            amount_of_adresses = minuend - subtrahend
            for i in range (amount_of_adresses):
                subtrahend = subtrahend + 1
                ready_address_splitted = ready_address.split('.')
                ready_address_splitted[-1] = str(subtrahend)
                ready_address = '.'.join(ready_address_splitted)
                distinct_addresses.append(ready_address)
        elif '-' in split_checker[3] and len(split_checker) == 4:
            splitted_address1 = address.split('-')
            minuend1 = int(splitted_address1[1])
            oktets_of_subtrahend1 = splitted_address1[0].split('.')
            subtrahend1 = int(oktets_of_subtrahend1[-1])
            ready_address1 = str(splitted_address1[0])
            distinct_addresses.append(ready_address1)
            amount_of_adresses1 = minuend1 - subtrahend1
            for j in range (amount_of_adresses1):
                subtrahend1 = subtrahend1 + 1
                ready_address_splitted1 = ready_address1.split('.')
                ready_address_splitted1[-1] = str(subtrahend1)
                ready_address1 = '.'.join(ready_address_splitted1)
                distinct_addresses.append(ready_address1)
        else:
            distinct_addresses.append(address)

    return distinct_addresses

print(convert_ranges_to_ip_list(ips))