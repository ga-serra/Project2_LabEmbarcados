from machine import Pin, ADC


class Photoresistor:
    def __init__(self, pin):
        self.analog = ADC(Pin(pin))

    def read_sensor(self):
        # read the voltage and return a value between 0 and 1
        digital_value = self.analog.read_u16() 
        value = 1 - digital_value / 65535             
        return value
