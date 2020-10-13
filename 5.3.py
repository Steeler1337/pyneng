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
vlan = input('Enter vlan number(s): ')



print('\n' + '-' * 30)
print('interface {}'.format(interface))

if mode == 'access':
    print('\n'.join(access_template).format(vlan))
elif mode =='trunk':
    print('\n'.join(trunk_template).format(vlan))

