import ifcfg
import time
import platform
import os
import psutil
import speedtest_cli as speedtest
import colorama
from colorama import Fore, Style

if platform.system() == 'Linux':
    os.system("clear")
    
elif platform.system() =='Windows':
    os.system("cls")

colorama.init()
print(Fore.MAGENTA)

pattern = ''' 
 __       __ ______ ________ ______      ______ __    __ ________  ______  
|  \  _  |  \      \        \      \    |      \  \  |  \        \/      \ 
| ▓▓ / \ | ▓▓\▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓\▓▓▓▓▓▓     \▓▓▓▓▓▓ ▓▓\ | ▓▓ ▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓
| ▓▓/  ▓\| ▓▓ | ▓▓ | ▓▓__     | ▓▓        | ▓▓ | ▓▓▓\| ▓▓ ▓▓__   | ▓▓  | ▓▓
| ▓▓  ▓▓▓\ ▓▓ | ▓▓ | ▓▓  \    | ▓▓        | ▓▓ | ▓▓▓▓\ ▓▓ ▓▓  \  | ▓▓  | ▓▓
| ▓▓ ▓▓\▓▓\▓▓ | ▓▓ | ▓▓▓▓▓    | ▓▓        | ▓▓ | ▓▓\▓▓ ▓▓ ▓▓▓▓▓  | ▓▓  | ▓▓
| ▓▓▓▓  \▓▓▓▓_| ▓▓_| ▓▓      _| ▓▓_      _| ▓▓_| ▓▓ \▓▓▓▓ ▓▓     | ▓▓__/ ▓▓
| ▓▓▓    \▓▓▓   ▓▓ \ ▓▓     |   ▓▓ \    |   ▓▓ \ ▓▓  \▓▓▓ ▓▓      \▓▓    ▓▓
 \▓▓      \▓▓\▓▓▓▓▓▓\▓▓      \▓▓▓▓▓▓     \▓▓▓▓▓▓\▓▓   \▓▓\▓▓       \▓▓▓▓▓▓

        ⠠⠞⠑⠭⠞⠶⠠⠑⠙⠊⠞⠕⠗Github: https://github.com/suchsoak⠠⠞⠑⠭⠞⠶⠠⠑⠙⠊⠞⠕⠗
'''

print(pattern)
print(Style.RESET_ALL)

time.sleep(5.0)
        
interfaces = ifcfg.interfaces()

wifi = ['inet', 'netmask', 'device', 'inet4', 'netmasks', 'broadcast', 'broadcasts']

# Information

for interface in interfaces.values():
        if all(key in interface for key in wifi):
            if all(interface) is not None:
                print ("Inet:                   ",interface['inet'])
                print ("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
                colorama.init()
                print(Fore.MAGENTA)
                print ("Device:                 ",interface['device'])    
                print ("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
                print(Style.RESET_ALL)
                print ("Inet4:                  ",interface['inet4']) 
                print ("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
                print ("Inet6:                  ",interface['inet6']) 
                print ("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
                print ("Netmask:                ",interface['netmask'])
                print ("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
                print ("Netmasks:               ",interface['netmasks'])
                print ("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
                print ("Broadcast:              ",interface['broadcast'])
                print ("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
                print ("Broadcasts:             ",interface['broadcasts'])
                print ("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")

time.sleep(3.0)

print("\t")
colorama.init()
print(Fore.MAGENTA)
family = '''
.−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−.
| ⠠⠞⠑⠭⠞⠶⠠⠑⠙⠊⠞⠕⠗Family Information⠠⠞⠑⠭⠞⠶⠠⠑⠙⠊⠞⠕⠗ |
'−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−'
'''
print(family)
print(Style.RESET_ALL)
print("\t")
add = psutil.net_if_addrs()

for interface, addresses in add.items():
    print(f"Interface: {interface}")
    for address in addresses:
        print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        print("Family:", address.family)
        print("Address:", address.address)
        print("Netmask:", address.netmask)
        print("Broadcast:", address.broadcast)
print()

time.sleep(2.0)

# Speed Teste

try:
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()

    speed = s.results

    print("")

    colorama.init()

    print(Fore.MAGENTA)

    Speedtest = '''
    .−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−.
    | ⠠⠞⠑⠭⠞⠶⠠⠑⠙⠊⠞⠕⠗Speed teste⠠⠞⠑⠭⠞⠶⠠⠑⠙⠊⠞⠕⠗ | 
    '−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−'
    '''
    print(Speedtest)
    print(Style.RESET_ALL) 
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("Download:", speed.download / 1024 / 1024, "Mbps")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("Upload:", speed.upload / 1024 / 1024, "Mbps")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("Ping:", speed.ping, "ms")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("Server:", speed.server['sponsor'])

except Exception as error:
     print(error)
