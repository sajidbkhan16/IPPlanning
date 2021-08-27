import socket

def NetHostSplit(ip, mask):
      
    binary_ip = ''
    ip_list = ip.split('.')

    for octet in ip_list:
        octet_bin = bin(int(octet))[2:]
        octet_bin = octet_bin.zfill(8)
        binary_ip = binary_ip + octet_bin
                
    net_bits = binary_ip[:int(mask)]
    host_bits = binary_ip[int(mask):]
        
    return net_bits, host_bits


def ConverToIP(binary_ip):
    oct1 = int(binary_ip[0:8], 2)
    oct2 = int(binary_ip[8:16], 2)
    oct3 = int(binary_ip[16:24], 2)
    oct4 = int(binary_ip[24:32], 2)

    ip = '{}.{}.{}.{}'.format(oct1,oct2,oct3,oct4)

    return ip

def subnets(ip, mask):

    net, host = NetHostSplit(ip, mask)

    if len(net) == 32:
        host = 0

    if not int(host):
        
        # if host is '0' then subnet should be equal to IP (e.g 192.168.1.0)
        subnet = ip
         # current network addr should be equal original network. This is required to compute next IP block
        net_dec = int(net, 2)
    else:
            # if host is non zero then convert network to decimal and add 1 then re-convert to binary
        net_dec = int(net, 2)
        net_dec = net_dec + 1
        binary_ip_tmp = bin(net_dec)[2:].rjust(len(net), '0')
        binary_ip_tmp = binary_ip_tmp.ljust(32, '0')
        #print(binary_ip)
        # convert binary to standard IP format (e.g '11001000000000000000000000000000' to 192.168.1.0)
        subnet = ConverToIP(binary_ip_tmp)
            
    net_dec = net_dec + 1
        
    binary_ip = bin(net_dec)[2:].rjust(len(net), '0')
    binary_ip = binary_ip.ljust(32, '0')
        
    next_block = ConverToIP(binary_ip)
    return subnet, next_block

def ValidIP(ip):
	try:
		return bool(socket.inet_aton(ip))
	except:
		return False
   
    
