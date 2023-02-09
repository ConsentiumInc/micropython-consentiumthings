from ConsentiumThings import ThingsUpdate
import utime

api_key = ""

board = ThingsUpdate(key=api_key)

board.initWiFi("", "")

sensor_val = [1, 2, 3, 4, 5, 6, 7]
info_buff = ["a", "b", "c", "d", "e", "f", "g"]

while True:
    r = board.sendREST(sensor_val=sensor_val, info_buff=info_buff)
    print(r.text)
    utime.sleep(5)