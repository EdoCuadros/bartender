import RPi.GPIO as GPIO
import time
from interface import ESTADO, DataCoctel
from valv import init_pump, run_pump
from sensores import sensors

# PINES IN1
PUMPS:dict[str, int] = {
    "rum": 26,
    "sweetener": 17,
    "orange": 27,
    "lime": 22
    #"out": 0
}

MOTOR_PIN = 23

# TODO: Escribir la función para dispensar bebidas



def dispense(coctel: DataCoctel):


    # Sirve los ingredientes
    run_pump(PUMPS["rum"],coctel.rum, sensors)
    sensors.range

    # TODO: Actualiza estados de los ingredientes