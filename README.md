# uPythonAPI
This repo cointains code for MicroPython API

ESP 8266 test passing


# module installation 

```python
import upip
import network
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("", "")
station.isconnected()
print(station.ifconfig())

upip.install('micropython-urequests')
```
