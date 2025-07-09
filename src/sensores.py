from enum import Enum
import time
import board
import busio
import adafruit_vl53l0x
from smbus2 import SMBus        # para controlar el multiplexor

class SensorEnum(int, Enum):
    SENSOR_1 = 0
    SENSOR_2 = 1
    SENSOR_3 = 2


class sensorVL53L0X:
    def __init__(self, channel: SensorEnum, i2c_bus: busio.I2C, mux_dir: int):
        self.channel = channel
        self.i2c_bus = i2c_bus          # Para el sensor
        self.mux_dir = mux_dir          # Dirección I2C del multiplexor (por defecto 0x70)
        self.bus_control = SMBus(1)     # Controla el multiplexor
        self._select_channel()
        time.sleep(0.1)
        self.sensor = adafruit_vl53l0x.VL53L0X(i2c_bus)
        time.sleep(0.1)

    def _select_channel(self):
        """
        Activa el canal correspondiente al multiplexor I2C
        """
        if 0 <= self.channel.value <= 7:
            try:
                self.bus_control.write_byte(self.mux_dir, 1 << self.channel.value)
                time.sleep(0.05)
            except OSError as e:
                print(f"[ERROR] Canal {self.channel.name} no pudo activarse: {e}")

    def get_range(self) -> int:
        """
        Lee y retorna la distancia medida por el sensor
        """
        self._select_channel()
        return self.sensor.range
    
class Sensores:
    def __init__(self, i2c_bus: busio.I2C, mux_dir: int = 0x70):
        self.i2c_bus = i2c_bus
        self.mux_dir = mux_dir
        self.sensores: dict[SensorEnum, sensorVL53L0X] = {}
        self._init_sensores()

    def _init_sensores(self):
        for channel in SensorEnum:
            self.sensores[channel] = sensorVL53L0X(channel, self.i2c_bus, self.mux_dir)

    def get_level(self, channel: SensorEnum) -> int:
        return self.sensores[channel].get_range()            
