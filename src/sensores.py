import time
import board
import busio
import adafruit_vl53l0x
from smbus2 import SMBus
    
MUX_ADDRESS = 0x70

control_bus = SMBus(1)

i2c = busio.I2C(board.SCL, board.SDA)
sensors = [None] * 4


def select_channel(channel):
    """
    Método para seleccionar canales del multiplexor. 
    Se activa el canal que se quiere leer y el resto se cierra.
    Input: 
    - channel: Canal del sensor que se quiere leer
    """
    if 0 <= channel <= 4:       # 4 sensores de nivel conectados por i2c
        control_bus.write_byte(MUX_ADDRESS, 1 << channel)
        time.sleep(0.5)

def init_sensors():
    """
    Se inicializan los sensores creando un objeto para cada uno   
    y guardandolo en el vector 'sensors'
    """
    global sensors

        #select_channel(channel)
    sensors = adafruit_vl53l0x.VL53L0X(i2c)
    time.sleep(0.1)


def getLevel(channel):
    """
    Se hace lectura del canal deseado
    """
    #select_channel(channel)
    return sensors.range

