from w1thermsensor import W1ThermSensor, Unit

sensor = W1ThermSensor()
temperature_C = sensor.get_temperature()
print(temperature_C)
