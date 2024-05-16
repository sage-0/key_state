import network
import time
import urequests as requests
from machine import Pin

#Pin
p33 = Pin(33, Pin.IN)

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
    last_state = bool(p33.value())
    do_connect()
    while True:
        current_state = bool(p33.value())
        if current_state != last_state:
            last_state = current_state
            state_text = "Opened" if current_state else "Closed"
            payload = f"""content={state_text}"""
            response = requests.post(URL, headers={"Content-Type": "application/x-www-form-urlencoded"}, data=payload)
            response.close()
            time.sleep(10)

main()