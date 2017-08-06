from w1thermsensor import W1ThermSensor


for sensor in W1ThermSensor.get_available_sensors():
    print('Sensor %s has temperature %.2f' % (sensor.id, sensor.get_temperature()))

outside = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, '0316b578daff')
inside = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, '0416c215a0ff')

print('outside: {}'.format(outside.get_temperature()))
print('inside: {}'.format(inside.get_temperature()))


