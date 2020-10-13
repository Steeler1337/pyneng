from sys import argv

#10.1.1.195/28

address_string = argv[1]

ip = address_string[0:address_string.find('/')]
ip_splitted = ip.split('.')

bin_ip_full = ''

bin_ip_0b = bin(int(ip_splitted[0]))
bin_ip = bin_ip_0b[2::]
bin_ip_full = bin_ip_full + '0' * (8 - len(bin_ip)) + bin_ip
bin_ip_0b = bin(int(ip_splitted[1]))
bin_ip = bin_ip_0b[2::]
bin_ip_full =  bin_ip_full + '0' * (8 - len(bin_ip)) + bin_ip
bin_ip_0b = bin(int(ip_splitted[2]))
bin_ip = bin_ip_0b[2::]
bin_ip_full =  bin_ip_full + '0' * (8 - len(bin_ip)) + bin_ip
bin_ip_0b = bin(int(ip_splitted[3]))
bin_ip = bin_ip_0b[2::]
bin_ip_full = bin_ip_full + '0' * (8 - len(bin_ip)) + bin_ip

mask = address_string[address_string.find('/') + 1::]
bin_ip_full_net = bin_ip_full[0 : int(mask)] + '0' * (32 - int(mask))

ip_splitted[3]  = int(bin_ip_full_net[24:32], 2)
#print('Последний октет: ' + str(ip_splitted[3]))


#print('Хост: ' + bin_ip_full)
#print('Сеть: ' + bin_ip_full_net)



print('\nNetwork:')
information = '''
    {0:<8} {1:<8} {2:<8} {3:<8}
    {0:08b} {1:08b} {2:08b} {3:08b}
    '''
print(information.format(int(ip_splitted[0]), int(ip_splitted[1]), int(ip_splitted[2]), int(ip_splitted[3])))

mask2 = address_string[address_string.find('/')::]
print('\nMask:')
print(mask2)
mask_number = mask2[1::]
binary_mask = '1' * int(mask_number) + '0' * (32 - int(mask_number))
first_okt_mask = binary_mask[0:8]
first_okt_number = int(first_okt_mask, 2)
second_okt_mask = binary_mask[8:16]
second_okt_number = int(second_okt_mask, 2)
third_okt_mask = binary_mask[16:24]
third_okt_number = int(third_okt_mask, 2)
fourth_okt_mask = binary_mask[24:32]
fourth_okt_number = int(fourth_okt_mask, 2)

information2 = '''
    {0:<8} {1:<8} {2:<8} {3:<8}
    {4:<8} {5:<8} {6:<8} {7:<8}
'''
print(information2.format(first_okt_number, second_okt_number, third_okt_number, fourth_okt_number, first_okt_mask, second_okt_mask, third_okt_mask, fourth_okt_mask))



