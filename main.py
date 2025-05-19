from machine import Pin, UART
from utime import sleep
from servo import Servo
import time

pin = Pin(13, Pin.OUT)

bluetooth = UART(0, baudrate=115200, tx=Pin(16), rx=Pin(17))

servo = Servo(8)

while True:
    if bluetooth.any():
        msg = bluetooth.read()
        print(msg)

    servo.set_angle(90)
    time.sleep(1)
    servo.set_angle(0)
    time.sleep(1)
    servo.write_angle(180)
    time.sleep(1)

# The program should never reach here
pin.off()
print("Finished.")
