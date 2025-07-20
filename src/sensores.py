from enum import Enum
import time
import board
import busio
import adafruit_vl53l0x
from smbus2 import SMBus        # para controlar el multiplexor
import numpy as np

class SensorEnum(int, Enum):
    rum_sensor  = 0
    lime_sensor = 1
    orange_sensor = 2
    sweetener_sensor = 3

class sensorVL53L0X:
    def __init__(self, channel: SensorEnum, i2c_bus: busio.I2C, mux_dir: int):
        self.channel = channel
        self.i2c_bus = i2c_bus          # Para el sensor
        self.mux_dir = mux_dir          # Dirección I2C del multiplexor (por defecto 0x70)
        self.bus_control = SMBus(1)     # Controla el multiplexor
        self.altura_vaso = 0.1 #   [m]
        self.radio_menor = 0.053    # [m]
        self.radio_mayor = 0.09
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
    
    @property
    def get_volume(self) -> float:
        """
        Usa la función get_range para leer la altura y lo convierte en volumen.
        """
        h_prime = self.get_range() 
        R_prime = self.radio_mayor * (self.altura_vaso - h_prime) / self.altura_vaso

        # Conversión de altura sensada a volumen de liquido restante
        return 1 / 3 * np.pi * (self.altura_vaso - h_prime) * (
            R_prime ** 2 + self.radio_menor ** 2 + R_prime * self.radio_menor)  
    
class Sensores:
    def __init__(self, i2c_bus: busio.I2C, mux_dir: int = 0x70):
        self.i2c_bus = i2c_bus
        self.mux_dir = mux_dir
        self._init_sensores()

    def _init_sensores(self):
        self.rum = sensorVL53L0X(SensorEnum.rum_sensor, self.i2c_bus, self.mux_dir)
        self.lime = sensorVL53L0X(SensorEnum.lime_sensor, self.i2c_bus, self.mux_dir)
        self.orange = sensorVL53L0X(SensorEnum.orange_sensor, self.i2c_bus, self.mux_dir)
        self.sweetener = sensorVL53L0X(SensorEnum.sweetener_sensor, self.i2c_bus, self.mux_dir)

    """
    def get_volume(self, sensor : sensorVL53L0X) -> float:
        h_prime = sensor.get_range 
        R_prime = self.radio_mayor * (self.altura_vaso - h_prime) / self.altura_vaso

        # Conversión de altura sensada a volumen de liquido restante
        return 1 / 3 * np.pi * (self.altura_vaso - h_prime) * (
            R_prime ** 2 + self.radio_menor ** 2 + R_prime * self.radio_menor)  
    """