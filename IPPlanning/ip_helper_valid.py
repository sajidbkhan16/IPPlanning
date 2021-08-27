import os
import pandas as pd
import re
from itertools import combinations

ptrn_ip = r'\d+\.\d+\.\d+\.\d+\/\d+'

def NetHostSplit(ip):   
    binary_ip = ''
    ip_list_temp = ip.split('.')
    fourth_oct, mask = ip_list_temp[3].split('/')
    ip_list = ip_list_temp[:3] + [fourth_oct]

    for octet in ip_list:
            octet_bin = bin(int(octet))[2:]
            l = 8 - len(octet_bin)
            for i in range(l):
                        octet_bin = '0' + octet_bin
            binary_ip = binary_ip + octet_bin
               
    net_bits = binary_ip[:int(mask)]
    host_bits = binary_ip[int(mask):]
            
    return net_bits, host_bits

def Sanity(ip):
    flag_err = 0    
    net_bits, host_bits = NetHostSplit(ip)
    
    if len(net_bits) != 32:
        if int(host_bits):
            print("error occured.{} is incorrect subnet".format(ip))
            flag_err = 1
        
    return flag_err

def ValidateList(ip_list):
    flag_list = []
    flag_subnet_list = []
    
    for ip in ip_list:
        if re.match(ptrn_ip, ip):
            flag = Sanity(ip)
            flag_list.append(flag)
        
    if max(flag_list) == 0:
        print('Subnets are valid. Successfully verified')

def ValidateIPConflict(ip_list):
    flag_subnet_list = []
    ip_pair_list = list(combinations(ip_list, 2))

    for ip_pair in ip_pair_list:
        if re.match(ptrn_ip, ip_pair[0]) and re.match(ptrn_ip, ip_pair[1]):
            net_bits_1, _ = NetHostSplit(ip_pair[0])
            net_bits_2, _ = NetHostSplit(ip_pair[1])

            mask = min(len(net_bits_1), len(net_bits_2))
            net_bits_1 = net_bits_1[:mask]
            net_bits_2 = net_bits_2[:mask]
        
            if net_bits_1 != net_bits_2:
                flag_subnet_list.append(0)
            else:                
                flag_subnet_list.append(1)
                print('Conflict detected in following pair {}'.format(ip_pair))
                
    if max(flag_subnet_list) == 0:
        print('No conflict detected')
