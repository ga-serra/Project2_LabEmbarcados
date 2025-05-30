from machine import Pin, ADC


class Photoresistor:
    def __init__(self, pin):
        self.analog = ADC(Pin(pin))

    """
    @brief Lê a tensão no fotoresistor através do ADC
    @return float Um valor entre 0.0 e 1.0 tão maior quanto maior for
    a luminosidade
    """
    def read_sensor(self):
        digital_value = self.analog.read_u16() 
        value = 1 - digital_value / 65535             
        return value
