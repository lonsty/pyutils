# @Author: allen
# @Date: Apr 14 19:55 2020
import re


def is_valid_ipv4(ip):
    m = re.match(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$', ip)
    return bool(m) and all(map(lambda x: (not x.startswith('0') if len(x) >= 2 else True)
                                          and (0 <= int(x) <=255),
                               m.groups()))


def is_valid_netmask(ip):
    if is_valid_ipv4(ip):
        ns = ip.split('.')
        sbin = list(map(lambda n: bin(int(n))[2:].zfill(8), ns))
        s01 = ''.join(sbin)
        
        try:
            idx_0 = s01.index('0')
            idx_1 = s01[::-1].index('1')
            if idx_0 + idx_1 != len(s01):
                return False
        except ValueError:
            return False
        
        return True
    
    return False
