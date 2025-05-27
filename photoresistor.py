from machine import Pin, ADC


class photoresistor:
    def __init__(self, pin):
        self.analog = ADC(Pin(pin))

    def read_sensor(self):
        # return value between 0 and 65535
        
        digital_value = self.analog.read_u16() 
        return digital_value