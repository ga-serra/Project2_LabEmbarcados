from machine import Pin, PWM

class Servo:
    def __init__(self, pin_num:int, freq:int = 50):
        self.pwm = PWM(Pin(pin_num))
        self.pwm.freq(freq)

    def set_angle(self, angle):
        # Angle has to be between 0º and 180º
        if angle < 0:
            angle = 0
        elif angle > 180:
            angle = 180

        # angle for time (pulse)
        min_time = 500                  # minimum pulse time
        max_time = 2500                 # maximum pulse time
        time_us = min_time + (angle/180) * (max_time - min_time)

        # Set duty cycle
        duty_cycle = int(time_us * 65535 / 20000)
        self.pwm.duty_u16(duty_cycle)
