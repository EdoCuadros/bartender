import RPi.GPIO as GPIO
import time
from valv import init_pump, run_pump


# PINES [EN, IN1]
PUMPS = {
    "rum": [0, 0],
    "sweetener": [0, 0],
    "orange": [0, 0],
    "lime": [0, 0],
    "out": [0, 0]
}


MOTOR_PIN = 23

# TODO: Escribir la función para dispensar bebidas

def dispense(drink_dict):

    # Sirve los ingredientes
    for ingredient in drink_dict.keys():
        run_pump(PUMPS[ingredient])

    # TODO: Actualiza estados de los ingredientes