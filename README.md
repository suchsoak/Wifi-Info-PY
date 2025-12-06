# 🌐 Wifi-Info-PY

**A script that provides detailed WiFi network information**

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
```

**👤 Author:** [suchsoak](https://github.com/suchsoak) | **📦 Version:** v1.0.5

---

## 📥 Installation

>[!NOTE]
> Don't forget to install `requirements.txt`

```sh
git clone https://github.com/suchsoak/Wifi-Info-PY
cd Wifi-Info-PY
pip install -r requirements.txt
```

**On linux | Ubuntu / Debian / Kali Linux / Linux Mint:**
```sh
sudo apt update && sudo apt install -y net-tools
```

---

## 🚀 Usage

```sh
python3 wifiinfo.py
```

---

## 📡 WiFi Device Function

Shows networks that have already been connected.

>[!IMPORTANT]
> Requires `network-manager` installed on your system for full functionality

```sh
wifi_info = nt.device.wifi()

for device in wifi_info:
    wifi_mode = device.mode
    wifi_bssid = device.bssid
    wifi_ssid = device.ssid
```

**Without nmcli**, the script runs normally with reduced functionality.

---

## 🔥 Firewall Test

Tests connection to the Tor Project to detect firewall issues:

```sh
r = requests.get('https://www.torproject.org/')
```

### HTTP Status Codes

| Code | Meaning |
|------|---------|
| **200** | ✅ OK - Successful request |
| **403** | 🚫 Forbidden - Access denied |
| **404** | ❌ Not Found - Resource unavailable |
| **503** | ⚠️ Service Unavailable - Server busy/maintenance |

---

## ⚡ Speed Test

Conversion formula: `results.upload/1024/1024` (bytes → Mbps)

```sh
print("Download:", speed.download / 1024 / 1024, "Mbps")
print("Upload:", speed.upload / 1024 / 1024, "Mbps")
```

**Alternative units:** Use `1000` for Kbps or `1024/1024` for Gbps.

---

## 📚 Libraries

| Library | Link |
|---------|------|
| 📊 Psutil | https://pypi.org/project/psutil/ |
| ⚡ Speedtest | https://github.com/sivel/speedtest-cli/wiki |
| 🔧 Ifcfg | https://pypi.org/project/ifcfg/ |
| 🖥️ nmcli | https://github.com/ushiboy/nmcli |
| 🎨 Colorama | https://pypi.org/project/colorama/ |
| 📖 Platform | https://docs.python.org/3/library/platform.html |

---

## 📄 License

`GPL-3.0 license`
