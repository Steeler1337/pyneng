ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

splitted = ospf_route.split()
zero = splitted[0]
first = splitted[1].strip('[]')
third = splitted[3].rstrip(',')
fourth = splitted[4].rstrip(',')
fifth = splitted[-1]

info = '''
    {0:<22} {1:<22} 
    {2:<22} {3:<22}
    {4:<22} {5:<22}
    {6:<22} {7:<22}
    {8:<22} {9:<22}
    '''
   
print(info.format('Prefix', zero, 'AD/Metric', first, 'Next-Hop', third, 'Last update', fourth, 'Outbound Interface', fifth))

