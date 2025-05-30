from machine import Pin, UART
import photoresistor
from utime import sleep
from servo import Servo
import time
from dht import DHT11, InvalidCheckSum
from photoresistor import Photoresistor

# =================== VARIÁVEIS GLOBAIS ==========================

led_pin = Pin(13, Pin.OUT)
dht_pin = Pin(4, Pin.OUT, Pin.PULL_DOWN)

bluetooth = UART(0, baudrate=115200, tx=Pin(16), rx=Pin(17))
servo = Servo(8)
dht_sensor = DHT11(dht_pin)
photoresistor = Photoresistor(28)

# ======================= FUNÇÕES ==========================
"""
@brief Realiza ações de acordo com um comando msg:
    "report": envia os dados de temperatura e umidade por bluetooth
    "abre": move o servo-motor para 90º (efetivamente abre a porta)
    "fecha": move o servo-motor para 0º (efetivamente fecha a porta)
"""
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


"""
@brief Checa a iluminação atual e compara com um valor `threshold`. Se a 
iluminação é menor que `threshold`, o LED (iluminação artificial) é ativado.
Caso contrário, ele é desativado.

@param threshold: float Valor limite para o 
@pre threshold >= 0.0
@pre threshold <= 1.0
"""
def check_lighting(threshold):
    light_meas = photoresistor.read_sensor()
    if(light_meas <= threshold):
        led_pin.value(1)
    else:
        led_pin.value(0)

def main():
    thresh = 0.5
    while True:
        check_lighting(thresh)
        if bluetooth.any():
            msg = bluetooth.read().decode('utf-8')
            handle_command(msg)

    # O programa nunca deve chegar aqui
    led_pin.value(0)
    print("Finished.")

if __name__ == '__main__':
    main()
