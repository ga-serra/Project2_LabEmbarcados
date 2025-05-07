from machine import Pin, UART
from utime import sleep

pin = Pin(13, Pin.OUT)

bluetooth = UART(0, baudrate=115200, tx=Pin(16), rx=Pin(17))

while True:
    if bluetooth.any():
        msg = bluetooth.read()
        print(msg)
pin.off()
print("Finished.")
