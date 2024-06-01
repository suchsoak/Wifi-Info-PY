# Wifi-Info-PY

**The script that gives information about WIFI**

[![Update](https://github.com/suchsoak/Wifi-Info-PY/actions/workflows/update.yml/badge.svg)](https://github.com/suchsoak/Wifi-Info-PY/actions/workflows/update.yml)

```sh
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
                                            BY:suchsoak
                                              v:1.0.4
```

# How to install

>[!NOTE]
> Don't forget to install the requirements.txt

```sh
  git clone https://github.com/suchsoak/Wifi-Info-PY
```

```sh
  cd Wifi-Info-PY
```

```sh
  pip install -r requirements.txt
```

# Usage

```sh
  python3 wifiinfo.py
```

# How nt.device.wifi works

**it will show networks that have already been connected**

>[!IMPORTANT]
> For nmcli to work you need to have in your network-manager system

```sh
wifi_info = nt.device.wifi()

for device in wifi_info:
    try:
        wifi_mode = device.mode
        wifi_bssid = device.bssid
        print()
        wifi_ssid = device.ssid
        print()
        ...
```
#### If you don't have nmcli, the script will run normally, just without the nmcli or network-manager function

```sh
search = os.system("nmcli")

if search == False:
   ...
```

It will look for the nmcli command, if not, just go to the next command in the script

```sh
else:
    pass
    ...
```

# How Firewall Test works

It will try to make the connection with the tor project, if this rejects the problem it may be because of the firewall. In case it may just be the error connection.

```sh
   r = requests.get('https://www.torproject.org/')
```
If you want, you can change the sites for make the requests.

```sh
    proxy = requests.get('https://www.proxysite.com/')
    vpnproton = requests.get('https://protonvpn.com/')
    proxylist = requests.get('https://free-proxy-list.net/')
    ...
```
## Status Code

The `HTTP 200` OK is the status response code from a server for successful `HTTP` requests from a client (browser). For a web page, it indicates that its HTML code can be loaded successfully. 

The `HTTP 403` is an **HTTP** status code meaning access to the requested resource is forbidden. The server understood the request, but will not fulfill it, if it was correct

The `404` error is an HTTP response code that indicates that the client was able to communicate with the server, but the server could not find what was requested, or was configured to not fulfill the request and not reveal the reason, the page no longer exists or the URL was entered incorrectly.

The `503` Service Unavailable error is an `HTTP` status code that means a website's server is not available right now. Most of the time, it occurs because the server is too busy or maintenance is being performed on it. 

# How speedtest works

The expression `results.upload/1024/1024` is used to convert the upload speed from bytes to megabits per second (Mbps). The value `1024` is used to convert bytes to kilobytes, and the value `1024` is used again to convert kilobytes to megabytes. If you want to change the number used in the conversion, you can change the `1024` values to other numbers. For example, if you want to convert bytes to gigabits per second **(Gbps)**, you can use `1024 / 1024` as the divisor. Or if you want to use a different unit, such as kilobits per second `(Kbps)`, you can use a smaller splitter, such as `1024/8`. Here is the example updated with a divisor of 1000 to convert to kilobits per second `(Kbps): print("Upload:", results.upload / 1000, "Kbps")` Keep in mind that when you change the splitter, you'll also need to adjust the unit of measurement in print.

```sh
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("Download:", speed.download / 1024 / 1024, "Mbps")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("Upload:", speed.upload / 1024 / 1024, "Mbps")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    ...
```
**If you want, you can change**

```sh
    print("Upload:", speed.upload / 1000, "Kbps")
```

# License & Copyright

`GPL-3.0 license`

## Libraries:

| Libraries |  Links |
| ------ | ------ |
| Psutil | https://pypi.org/project/psutil/
| Speedtest |  https://github.com/sivel/speedtest-cli/wiki
| Ifcfg |  https://pypi.org/project/ifcfg/
| nmcli |  https://github.com/ushiboy/nmcli
| Colorama |  https://pypi.org/project/colorama/
| Platform |  https://docs.python.org/3/library/platform.html
