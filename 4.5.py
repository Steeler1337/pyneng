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