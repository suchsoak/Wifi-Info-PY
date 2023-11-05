import ifcfg
import time
import psutil
import nmcli as nt
import requests 
import speedtest_cli as speedtest
import colorama
from colorama import Fore, Style

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
                                    v:1.0.2
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

# Family Information

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
        time.sleep(2)
        print("Netmask:", address.netmask)
        print("Broadcast:", address.broadcast)
print()

time.sleep(2.0)

colorama.init()
print(Fore.MAGENTA)

nt1 = '''
.−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−.
| ⠠⠞⠑⠭⠞⠶⠠⠑⠙⠊⠞⠕⠗Other Wifi Information⠠⠞⠑⠭⠞⠶⠠⠑⠙⠊⠞⠕⠗ |
'−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−'
'''
print(nt1)
print(Style.RESET_ALL)

wifi_info = nt.device.wifi()

for device in wifi_info:
    try:
        wifi_mode = device.mode
        wifi_bssid = device.bssid
        print()
        wifi_ssid = device.ssid
        print()
        time.sleep(3)
        wifi_signal = device.signal
        wifi_cha = device.chan
        wifi_frequency = device.freq
        wifi_security = device.security
        
        print(f"WiFi Mode: {wifi_mode}")
        print(f"BSSID: {wifi_bssid}")
        colorama.init()
        print(Fore.MAGENTA)
        print(f"SSID: {wifi_ssid}")
        print(Style.RESET_ALL)
        print(f"Signal Strength: {wifi_signal}")
        print(f"WiFi Chang: {wifi_cha}")
        print(f"wifi Frequency: {wifi_frequency}")
        print(f"wifi Security: {wifi_security}")
        print()
    except Exception as error:
        print(f"Error: {error}")
print("\t")

colorama.init()
print(Fore.MAGENTA)

# Firewall Test

firewall = '''
.−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−.
| ⠠⠞⠑⠭⠞⠶⠠⠑⠙⠊⠞⠕⠗Firewall Test⠠⠞⠑⠭⠞⠶⠠⠑⠙⠊⠞⠕⠗ |
'−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−'
'''
print(firewall)
print(Style.RESET_ALL)

try:

    r = requests.get('https://www.torproject.org/')
    proxy = requests.get('https://www.proxysite.com/')
    vpnproton = requests.get('https://protonvpn.com/')
    r.status_code

    if r.status_code == 200:
        colorama.init()
        print(Fore.MAGENTA)
        print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        print()
        print("Tor is not blocked!", "Status Code: " ,r.status_code)
        print()
        print("Proxy is not blocked!", "Status Code: " ,proxy.status_code)
        print()
        print("Vpnproton is not blocked!", "Status Code: " ,vpnproton.status_code)
        print()
        print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        print(Style.RESET_ALL) 

    elif r.status_code == 403:
        print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        print()
        print("Tor is not found", "Status Code: " ,r.status_code)
        print()
        print("Proxy is not found!", "Status Code: " ,proxy.status_code)
        print()
        print("vpnproton is not found!", "Status Code: " ,vpnproton.status_code)
        print()
        print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")

    elif r.status_code == 503:
        print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        print()
        print("Tor is not found", r.status_code)
        print()
        print("Proxy is not found!", "Status Code: " ,proxy.status_code)
        print()
        print("vpnproton is not found!", "Status Code: " ,vpnproton.status_code)
        print()
        print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        
    else:
        colorama.init()
        print(Fore.RED)
        print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        print()
        print("Tor rejected, bocked for firewall: ", r.status_code)
        print()
        print("Proxy blocked for firewall", "Status Code: " ,proxy.status_code)
        print()
        print("vpnproton blocked for firewall", "Status Code: " ,proxy.status_code)
        print()
        print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        print(Style.RESET_ALL)

except Exception as e:
    print(e)

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
