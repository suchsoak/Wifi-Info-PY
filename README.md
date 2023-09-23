# Wifi-Info-PY
 The script that gives information about WIFI

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
```

# How to install

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

# How to use

```sh
  python3 wifiinfo.py
```

# How speedtest works

The expression results.upload/1024/1024 is used to convert the upload speed from bytes to megabits per second (Mbps). The value 1024 is used to convert bytes to kilobytes, and the value 1024 is used again to convert kilobytes to megabytes. If you want to change the number used in the conversion, you can change the 1024 values to other numbers. For example, if you want to convert bytes to gigabits per second (Gbps), you can use 1024*1024*1024 as the divisor. Or if you want to use a different unit, such as kilobits per second (Kbps), you can use a smaller splitter, such as 1024/8. Here is the example updated with a divisor of 1000 to convert to kilobits per second (Kbps): print("Upload:", results.upload / 1000, "Kbps") Keep in mind that when you change the splitter, you'll also need to adjust the unit of measurement in print.

```sh
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("Download:", speed.download / 1024 / 1024, "Mbps")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
    print("Upload:", speed.upload / 1024 / 1024, "Mbps")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
```
If you want, you can change

```sh
print("Upload:", speed.upload / 1000, "Kbps")
```

## Libraries:

| Libraries |  Links |
| ------ | ------ |
| Psutil | https://pypi.org/project/psutil/
| Speedtest |  https://github.com/sivel/speedtest-cli/wiki
| Ifcfg |  https://pypi.org/project/ifcfg/
| Colorama |  https://pypi.org/project/colorama/
| Platform |  https://docs.python.org/3/library/platform.html



