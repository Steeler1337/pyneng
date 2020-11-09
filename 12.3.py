# -*- coding: utf-8 -*-
from tabulate import tabulate
"""
Задание 12.3
Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.
Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов
Результат работы функции - вывод на стандартный поток вывода таблицы вида:
Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9
Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.
Для этого задания нет тестов
"""


Reachable = ['10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.4']
Unreachable = ['10.1.1.7', '10.1.1.8', '10.1.1.9', '10.1.1.10', '10.1.1.11']

def print_ip_table(reachable_list, unreachable_list):
    columns = []
    alternation = []
    resultik = {}
    if len(reachable_list) >= len(unreachable_list):
        columns=['Reachable', 'Uneachable']
        resultik = dict.fromkeys(reachable_list)
        i = 0
        max_i = len(unreachable_list) - 1
        for addr in reachable_list:
            if i <= max_i:
                resultik[addr] = unreachable_list[i]
                i += 1
        for addr in reachable_list:
            if resultik[addr] is None:
                resultik[addr] = ''
        for k, v in resultik.items():
            temp = [k, v]
            alternation.append(temp)
    else:
        columns=['Unreachable', 'Reachable']
        resultik = dict.fromkeys(unreachable_list)
        i = 0
        max_i = len(reachable_list) - 1
        for addr in unreachable_list:
            if i <= max_i:
                resultik[addr] = reachable_list[i]
                i += 1
        for addr in unreachable_list:
            if resultik[addr] is None:
                resultik[addr] = ''
        for k, v in resultik.items():
            temp = [k, v]
            alternation.append(temp)
    print(tabulate(alternation, headers=columns))
    
print_ip_table(Reachable, Unreachable)