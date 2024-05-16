import network
import time
import urequests as requests
from machine import Pin

#Pin
p33 = Pin(33, Pin.IN)
status = Pin(2, Pin.OUT)

# AP
SSID = ""
PASS = ""

# discord webhook url
URL = "webhook url"

# Wifi
wlan = network.WLAN(network.STA_IF)

def do_connect():
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(SSID, PASS)
        while not wlan.isconnected():
            status.value(0)
            time.sleep(0.5)
            status.value(1)
    print('network config:', wlan.ifconfig())
    status.value(1)
    return

def main():
    last_state = bool(p33.value())
    do_connect()
    while True:
        try:
            if not wlan.isconnected():
                do_connect()
            current_state = bool(p33.value())
            if current_state != last_state:
                last_state = current_state
                state_text = "Opened" if current_state else "Closed"
                payload = f"""content={state_text}"""
                response = requests.post(URL, headers={"Content-Type": "application/x-www-form-urlencoded"}, data=payload)
                response.close()
                time.sleep(10)
        except Exception as e:
            print(f"Error: {e}")
            status.value(0)


main()