from w1thermsensor import W1ThermSensor, Unit


def getTemp():        
    sensor = W1ThermSensor()
    temperature_C = sensor.get_temperature()
    return temperature_C
