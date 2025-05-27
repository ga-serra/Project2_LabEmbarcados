from machine import Pin, UART
from utime import sleep
from servo import Servo
import time
from dht import DHT11, InvalidCheckSum
from PicoDHT22 import PicoDHT22


# Um número entre 0 e 1 que indica a que nível de luminosidade a lâmpada será acesa
LIGHT_THRESHOLD = 0.5

led_pin = Pin(13, Pin.OUT)
dht_pin = Pin(4, Pin.OUT, Pin.PULL_DOWN)

bluetooth = UART(0, baudrate=115200, tx=Pin(16), rx=Pin(17))
servo = Servo(8)
dht_sensor = DHT11(dht_pin)

def handle_command(msg):
    if msg == "report\r\n":
        try:
            temp, hum = dht_sensor.measure()
            bluetooth.write("Temperature: ")
            bluetooth.write(str(temp))
            bluetooth.write(" C\r\n")
            bluetooth.write("Humidity: ")
            bluetooth.write(str(hum))
            bluetooth.write(" %\r\n")
        except Exception as e:
            bluetooth.write(f"Error reading ambient data: {e}\r\n")
    
    elif msg == "abre\r\n":
        servo.step_to_angle(90)

    elif msg == "fecha\r\n":
        servo.step_to_angle(0)


def read_light_sensor():
    return 0.7


def check_lighting():
    light_meas = read_light_sensor()
    if(light_meas <= LIGHT_THRESHOLD):
        led_pin.value(1)
    else:
        led_pin.value(0)


while True:
    check_lighting()
    if bluetooth.any():
        msg = bluetooth.read().decode('utf-8')
        handle_command(msg)

# The program should never reach here
led_pin.value(0)
print("Finished.")


