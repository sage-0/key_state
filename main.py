import network
import time
import urequests as requests
from machine import Pin

#Pin
p33 = Pin(33, Pin.IN)

# Flag
open_flag = None
is_sended_flag = False

# AP
SSID = ""
PASS = ""

# discord webhook url
URL = "webhook url"

def do_connect():

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(SSID, PASS)
        while not wlan.isconnected():
            time.sleep(1)
    print('network config:', wlan.ifconfig())

    return


def main():
    global open_flag, is_sended_flag

    last_state = p33.value()

    do_connect()
    while True:
        current_state = p33.value()

        if current_state != last_state:
            if current_state == 0:
                open_flag = True
            else:
                open_flag = False

            is_sended_flag = True
            last_state = current_state

        # if p33.value() == 0:
        #     open_flag = True
        #     is_sended_flag = True
        # elif p33.value() == 1:
        #     open_flag = False
        #     is_sended_flag = True

        if is_sended_flag:
            if open_flag:
                print("Open")
                payload = """content=OPEN"""
                response = requests.post(URL, headers={"Content-Type": "application/x-www-form-urlencoded"}, data=payload)
                response.close()
            else:
                print("Close")
                payload = """content=CLOSE"""
                response = requests.post(URL, headers={"Content-Type": "application/x-www-form-urlencoded"}, data=payload)
                response.close()

            is_sended_flag = False

        print(is_sended_flag)




main()

