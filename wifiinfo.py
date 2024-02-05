import ifcfg
import time
import psutil
import nmcli as nt
import requests 
import colorama
from colorama import Fore, Style
import speedtest_cli as speedtest
import os

clear = os.system("clear")

if clear == True:
    os.system("cls")
else:
    print()

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
                                   BY: suchsoak
                                    v:1.0.3
'''

print(pattern)
print(Style.RESET_ALL)

time.sleep(2.0)
        
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
                print ("prefixlens:              ",interface['prefixlens'])
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
        time.sleep(1)
        print("Netmask:", address.netmask)
        print("Broadcast:", address.broadcast)
print()

net_connections = psutil.net_connections()

for conn in net_connections:

    laddr = conn.laddr  
    raddr = conn.raddr  
    status = conn.status  
    pid = conn.pid  
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print(f"Local: {laddr.ip}:{laddr.port}")
    print(f"Status: {status}")
    print(f"PID: {pid}")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")

time.sleep(1.0)

colorama.init()
print(Fore.MAGENTA)

nt1 = '''

    |ooo===ooo===oooo==oooo===ooo===ooo===ooo|
    |===ooo===ooo========+==oo===ooo===ooo===|
    |====o====oo=+:... .     ..:+=oo===ooo===|
    |ooo===oo=:.      .......     .:=o====ooo|
    |====oo=:    .:::::::::::+::.    :+ooo===|
    |===oo:   .:+::.          ..:+:.   :=o===|
    |ooo==.  :+:    ..::++:::.    :+:  .==ooo|
    |===oo=+=+.   :+=+::::::+++:    +=+=oo===|
    |===ooo==.  :+:.          .:+.  :==ooo===|
    |ooo===ooo++:    .:+++::.    :++=oo===ooo|
    |===o====oo=.  :+oo+:::=o=:  .=o===o=o===|
    |===ooo===oo=++=o=.     +oo++=oo===ooo===|
    |ooo===ooo====ooo:      :=ooo===ooo===ooo|
    |o=o====oo==o=oo=o:.  ..==========o=====o|
    |===ooo===ooo====oo=++=ooo===ooo===ooo===|

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
        time.sleep(2)
        wifi_signal = device.signal
        wifi_cha = device.chan
        wifi_frequency = device.freq
        wifi_security = device.security
        wifi_general = device.general
        
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
        print(f"wifi general: {wifi_general}")
        print()

    except Exception as error:
        print(f"Error: {error}")
        
print("\t")

colorama.init()
print(Fore.MAGENTA)

# Firewall Test

firewall = '''
.−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−------.
| ⠠⠞⠑⠭⠞⠶⠠⠑⠙⠊⠞⠕⠗Firewall Test⠠⠞⠑⠭⠞⠶⠠⠑⠙⠊⠞⠕⠗ |
'−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−------'
'''
print(firewall)
print(Style.RESET_ALL)

try:

    r = requests.get('https://www.torproject.org/')
    proxy = requests.get('https://www.proxysite.com/')
    vpnproton = requests.get('https://protonvpn.com/')
    proxylist = requests.get('https://free-proxy-list.net/')
    proxylist2 = requests.get('https://www.proxyscrape.com/free-proxy-list')
    OnWorks = requests.get('https://www.onworks.net/')
    nordvpn = requests.get('https://nordvpn.com/')
    shodan = requests.get('https://www.shodan.io/')
    zoomeye = requests.get('https://www.zoomeye.org/')
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
        print("free-proxy-list is not blocked!", "Status Code: " ,proxylist.status_code)
        print()
        print("Proxy_list2 is not blocked!", "Status Code: " ,proxylist2.status_code)
        print()
        print("OnWork is not blocked!", "Status Code: " ,OnWorks.status_code)
        print()
        print("NordVpn is not blocked!", "Status Code: " ,OnWorks.status_code)
        print()
        print("shodan is not blocked!", "Status Code: " ,shodan.status_code)
        print()
        print("zoomeye is not blocked!", "Status Code: " ,zoomeye.status_code)
        print()
        print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        print(Style.RESET_ALL) 

    elif r.status_code == 403:
        colorama.init()
        print(Fore.RED)
        print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        print()
        print("Tor is not found", "Status Code: " ,r.status_code)
        print()
        print("Proxy is not found!", "Status Code: " ,proxy.status_code)
        print()
        print("vpnproton is not found!", "Status Code: " ,vpnproton.status_code)
        print()
        print("free-proxy-list is not blocked!", "Status Code: " ,proxylist.status_code)
        print()
        print("Proxy_list2 is not blocked!", "Status Code: " ,proxylist2.status_code)
        print()
        print("OnWork is not blocked!", "Status Code: " ,OnWorks.status_code)
        print()
        print("NordVpn is not blocked!", "Status Code: " ,nordvpn.status_code)
        print()
        print("shodan is not blocked!", "Status Code: " ,shodan.status_code)
        print()
        print("zoomeye is not blocked!", "Status Code: " ,zoomeye.status_code)
        print()
        print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        print(Style.RESET_ALL) 

    elif r.status_code == 503:
        colorama.init()
        print(Fore.RED)
        print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        print()
        print("Tor is not found", r.status_code)
        print()
        print("Proxy is not found!", "Status Code: " ,proxy.status_code)
        print()
        print("vpnproton is not found!", "Status Code: " ,vpnproton.status_code)
        print()
        print("free-proxy-list is not blocked!", "Status Code: " ,proxylist.status_code)
        print()
        print("Proxy_list2 is not blocked!", "Status Code: " ,proxylist2.status_code)
        print()
        print("OnWork is not blocked!", "Status Code: " ,OnWorks.status_code)
        print()
        print("NordVpn is not blocked!", "Status Code: " ,nordvpn.status_code)
        print()
        print("shodan is not blocked!", "Status Code: " ,shodan.status_code)
        print()
        print("zoomeye is not blocked!", "Status Code: " ,zoomeye.status_code)
        print()
        print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        print(Style.RESET_ALL) 
        
    else:
        colorama.init()
        print(Fore.RED)
        print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        print()
        print("Tor rejected, bocked for firewall: ", r.status_code)
        print()
        print("Proxy blocked for firewall", "Status Code: " ,proxy.status_code)
        print()
        print("vpnproton blocked for firewall", "Status Code: " ,vpnproton.status_code)
        print()
        print("free-proxy-list blocked for firewall", "Status Code: " ,proxylist.status_code)
        print()
        print("Proxy_list2 blocked for firewall!", "Status Code: " ,OnWorks.status_code)
        print()
        print("NordVpn blocked for firewall!", "Status Code: " ,nordvpn.status_code)
        print()
        print("shodan blocked! for firewall!", "Status Code: " ,shodan.status_code)
        print()
        print("zoomeye blocked! for firewall!", "Status Code: " ,zoomeye.status_code)
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

    print()

    colorama.init()

    print(Fore.MAGENTA)

    Speedtest = '''
    .−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−-------.
    | ⠠⠞⠑⠭⠞⠶⠠⠑⠙⠊⠞⠕⠗Speed teste⠠⠞⠑⠭⠞⠶⠠⠑⠙⠊⠞⠕⠗ | 
    '−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−-------'
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
    print("Bytes:", speed.bytes_received, "bytes")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("Server:", speed.server['sponsor'])
    

except Exception as error:
     print(error)
