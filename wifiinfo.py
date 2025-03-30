import os
import time

requiremtes = os.system("pip install -r requirements.txt")
    
if requiremtes:
        print("Install requirements.txt")
else:
        print("All requirements.txt installed")
        time.sleep(2.0)

import ifcfg
import psutil
import nmcli as nt
import speedtest_cli as speedtest
import requests 
import colorama
from colorama import Fore, Style

clear = os.system("clear")

if clear == True:
    os.system("cls")
else:
    print()

colorama.init()
print(Fore.MAGENTA)

pattern = r''' 
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
                                    v:1.0.5
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
        print("PTP (Point-to-Point):", address.ptp if hasattr(address, 'ptp') else "N/A")
        print("Is Loopback:", "Yes" if interface.startswith("lo") else "No")
        print("Is Up:", "Yes" if psutil.net_if_stats()[interface].isup else "No")
        print("Speed (Mbps):", psutil.net_if_stats()[interface].speed)
        print("MTU:", psutil.net_if_stats()[interface].mtu)
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

search = os.system("nmcli")

if search == False:

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
else:
    pass

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
    hide_me = requests.get('https://hide.me/')
    ultrasurf = requests.get('https://ultrasurf.us/')
    psiphon = requests.get('https://psiphon.ca/')
    cyberghost = requests.get('https://www.cyberghostvpn.com/')
    expressvpn = requests.get('https://www.expressvpn.com/')
    surfshark = requests.get('https://surfshark.com/')
    windscribe = requests.get('https://windscribe.com/')
    hotspotshield = requests.get('https://www.hotspotshield.com/')
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
        print("NordVpn is not blocked!", "Status Code: " ,nordvpn.status_code)
        print()
        print("shodan is not blocked!", "Status Code: " ,shodan.status_code)
        print()
        print("zoomeye is not blocked!", "Status Code: " ,zoomeye.status_code)
        print()
        print("Hide.me is not blocked!", "Status Code: " ,hide_me.status_code)
        print()
        print("Ultrasurf is not blocked!", "Status Code: " ,ultrasurf.status_code)
        print()
        print("Psiphon is not blocked!", "Status Code: " ,psiphon.status_code)
        print()
        print("CyberGhost is not blocked!", "Status Code: " ,cyberghost.status_code)
        print()
        print("ExpressVPN is not blocked!", "Status Code: " ,expressvpn.status_code)
        print()
        print("Surfshark is not blocked!", "Status Code: " ,surfshark.status_code)
        print()
        print("Windscribe is not blocked!", "Status Code: " ,windscribe.status_code)
        print()
        print("Hotspot Shield is not blocked!", "Status Code: " ,hotspotshield.status_code)
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
        print("Hide.me is not blocked!", "Status Code: " ,hide_me.status_code)
        print()
        print("Ultrasurf is not blocked!", "Status Code: " ,ultrasurf.status_code)
        print()
        print("Psiphon is not blocked!", "Status Code: " ,psiphon.status_code)
        print()
        print("CyberGhost is not blocked!", "Status Code: " ,cyberghost.status_code)
        print()
        print("ExpressVPN is not blocked!", "Status Code: " ,expressvpn.status_code)
        print()
        print("Surfshark is not blocked!", "Status Code: " ,surfshark.status_code)
        print()
        print("Windscribe is not blocked!", "Status Code: " ,windscribe.status_code)
        print()
        print("Hotspot Shield is not blocked!", "Status Code: " ,hotspotshield.status_code)
        print()
        print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        print(Style.RESET_ALL) 

    elif r.status_code == 404:
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
        print("free-proxy-list is not found!", "Status Code: " ,proxylist.status_code)
        print()
        print("Proxy_list2 is not found!", "Status Code: " ,proxylist2.status_code)
        print()
        print("OnWork is not found!", "Status Code: " ,OnWorks.status_code)
        print()
        print("NordVpn is not found!", "Status Code: " ,nordvpn.status_code)
        print()
        print("shodan is not found!", "Status Code: " ,shodan.status_code)
        print()
        print("zoomeye is not found!", "Status Code: " ,zoomeye.status_code)
        print()
        print("Hide.me is not found!", "Status Code: " ,hide_me.status_code)
        print()
        print("Ultrasurf is not found!", "Status Code: " ,ultrasurf.status_code)
        print()
        print("Psiphon is not found!", "Status Code: " ,psiphon.status_code)
        print()
        print("CyberGhost is not found!", "Status Code: " ,cyberghost.status_code)
        print()
        print("ExpressVPN is not found!", "Status Code: " ,expressvpn.status_code)
        print()
        print("Surfshark is not found!", "Status Code: " ,surfshark.status_code)
        print()
        print("Windscribe is not found!", "Status Code: " ,windscribe.status_code)
        print()
        print("Hotspot Shield is not found!", "Status Code: " ,hotspotshield.status_code)
        print()
        print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        print(Style.RESET_ALL) 

    elif r.status_code == 503:
            colorama.init()
            print(Fore.RED)
            print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
            print()
            print("Tor service unavailable", "Status Code: " ,r.status_code)
            print()
            print("Proxy service unavailable!", "Status Code: " ,proxy.status_code)
            print()
            print("vpnproton service unavailable!", "Status Code: " ,vpnproton.status_code)
            print()
            print("free-proxy-list service unavailable!", "Status Code: " ,proxylist.status_code)
            print()
            print("Proxy_list2 service unavailable!", "Status Code: " ,proxylist2.status_code)
            print()
            print("OnWork service unavailable!", "Status Code: " ,OnWorks.status_code)
            print()
            print("NordVpn service unavailable!", "Status Code: " ,nordvpn.status_code)
            print()
            print("shodan service unavailable!", "Status Code: " ,shodan.status_code)
            print()
            print("zoomeye service unavailable!", "Status Code: " ,zoomeye.status_code)
            print()
            print("Hide.me service unavailable!", "Status Code: " ,hide_me.status_code)
            print()
            print("Ultrasurf service unavailable!", "Status Code: " ,ultrasurf.status_code)
            print()
            print("Psiphon service unavailable!", "Status Code: " ,psiphon.status_code)
            print()
            print("CyberGhost service unavailable!", "Status Code: " ,cyberghost.status_code)
            print()
            print("ExpressVPN service unavailable!", "Status Code: " ,expressvpn.status_code)
            print()
            print("Surfshark service unavailable!", "Status Code: " ,surfshark.status_code)
            print()
            print("Windscribe service unavailable!", "Status Code: " ,windscribe.status_code)
            print()
            print("Hotspot Shield service unavailable!", "Status Code: " ,hotspotshield.status_code)
            print()
            print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
            print(Style.RESET_ALL) 
            
    else:
            colorama.init()
            print(Fore.RED)
            print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
            print()
            print("Tor rejected, blocked by firewall: ", r.status_code)
            print()
            print("Proxy blocked by firewall", "Status Code: " ,proxy.status_code)
            print()
            print("vpnproton blocked by firewall", "Status Code: " ,vpnproton.status_code)
            print()
            print("free-proxy-list blocked by firewall", "Status Code: " ,proxylist.status_code)
            print()
            print("Proxy_list2 blocked by firewall!", "Status Code: " ,proxylist2.status_code)
            print()
            print("OnWork blocked by firewall!", "Status Code: " ,OnWorks.status_code)
            print()
            print("NordVpn blocked by firewall!", "Status Code: " ,nordvpn.status_code)
            print()
            print("shodan blocked by firewall!", "Status Code: " ,shodan.status_code)
            print()
            print("zoomeye blocked by firewall!", "Status Code: " ,zoomeye.status_code)
            print()
            print("Hide.me blocked by firewall!", "Status Code: " ,hide_me.status_code)
            print()
            print("Ultrasurf blocked by firewall!", "Status Code: " ,ultrasurf.status_code)
            print()
            print("Psiphon blocked by firewall!", "Status Code: " ,psiphon.status_code)
            print()
            print("CyberGhost blocked by firewall!", "Status Code: " ,cyberghost.status_code)
            print()
            print("ExpressVPN blocked by firewall!", "Status Code: " ,expressvpn.status_code)
            print()
            print("Surfshark blocked by firewall!", "Status Code: " ,surfshark.status_code)
            print()
            print("Windscribe blocked by firewall!", "Status Code: " ,windscribe.status_code)
            print()
            print("Hotspot Shield blocked by firewall!", "Status Code: " ,hotspotshield.status_code)
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
    print("Bytes Received:", speed.bytes_received, "bytes")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("Bytes Sent:", speed.bytes_sent, "bytes")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("Server Sponsor:", speed.server['sponsor'])
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("Server Name:", speed.server['name'])
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("Server Country:", speed.server['country'])
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("Server Host:", speed.server['host'])
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("Server Latency:", speed.server['latency'], "ms")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("ISP:", speed.client['isp'])
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("Client IP:", speed.client['ip'])
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("Client Country:", speed.client['country'])
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")

except Exception as error:
     print(error)
