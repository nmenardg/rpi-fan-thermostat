import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor

import config


outside = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, '0316b578daff')
inside = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, '0416c215a0ff')

target_temp = float(config.fan_section['target_temp'])
print('target: ' + str(target_temp))

inside_temp = inside.get_temperature()
print('inside: ' + str(inside_temp))
outside_temp = outside.get_temperature()
print('outside: ' + str(outside_temp))

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)  # Relay

if target_temp < inside_temp and outside_temp < inside_temp\
        or target_temp > inside_temp and outside_temp > inside_temp:
    # Yes
    GPIO.output(8, True)
else:
    # No
    GPIO.output(8, False)
    GPIO.cleanup()
