import argparse

def netmask(address:str, mask:int):
    binaddr = ''
    for i in address.split('.'):
        binaddress = bin(int(i))[2:]
        flag = '0'
        key = 8 - len(binaddress)
        if key != 0:
            binaddress = key * flag + binaddress
        binaddr += binaddress


    # 计算网络号，和最后可用地址 (二进制形式)
    host_count = 2 ** (32 - mask) -2
    network_address = binaddr[:mask] + (32 - mask) * '0'
    last_address = binaddr[:mask] + (32 - mask) * '1'

    # 网络号，广播地址 (十进制形式)
    network = '.'.join([str(int(network_address[i:i+8], 2)) for i in range(0, 32, 8)])
    broadcast = '.'.join([str(int(last_address[i:i+8], 2)) for i in range(0, 32, 8)])
    
    # 第一个可用地址和最后一个可用地址
    first_address = network[:-1] + str((int(network[-1:]) + 1))
    last_address = broadcast[:-1] + str((int(broadcast[-1:]) - 1))
    
    return {
                'start_address': network,
        'end_address': last_address,
        'host_count': host_count,
        "first": first_address,
        "broadcast": broadcast
    }

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description='子网掩码计算器')
    parse.add_argument('-i', dest='i', required=True, help='Input IP address (e.g. 192.168.10.2)')
    parse.add_argument('-m', dest='m', type=int, required=True, help="Input mask (e.g. 25)")
    args = parse.parse_args()

    result = netmask(args.i, args.m)
    print('可用主机数量:', result['host_count'])
    print('起始IP地址(网络位):', result['start_address'])
    print('第一个可用地址IP', result['first'])
    print('结束IP地址:', result['end_address'])
    print('广播地址：', result['broadcast'])