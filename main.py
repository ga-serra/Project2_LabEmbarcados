from machine import Pin, UART
from utime import sleep
from servo import Servo
import time
from dht import DHT11, InvalidCheckSum

pin = Pin(13, Pin.OUT)
dht_pin = Pin(4, Pin.OUT, Pin.PULL_DOWN)

bluetooth = UART(0, baudrate=115200, tx=Pin(16), rx=Pin(17))
servo = Servo(8)
dht_sensor = DHT11(dht_pin)

while True:
    if bluetooth.any():
        msg = bluetooth.read()
        print(msg)

    temp = dht_sensor.temperature
    hum = dht_sensor.humidity
    print(f"Temperature: {temp}, Humidity: {hum}")
    time.sleep(0.5)

    # servo.set_angle(90)
    # time.sleep(1)
    # servo.set_angle(0)
    # time.sleep(1)
    # servo.write_angle(180)
    # time.sleep(1)


# The program should never reach here
pin.off()
print("Finished.")
