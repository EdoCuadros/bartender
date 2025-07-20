import RPi.GPIO as GPIO
import time
from interface import ESTADO, PUMPS, DataCoctel
from sensores import Sensores
from valv import run_pump
import threading

# TODO: Escribir la función para dispensar bebidas
def setpoint_def(quantity: int) -> float:
    """
    Se le pasa el requerimiento en mL del coctel y la cantidad actual de mL
    """

def dispense(coctel: DataCoctel, sensores: Sensores):
    threads = []

    threads.append(threading.Thread(target=run_pump, args=(PUMPS["rum"], coctel.rum, sensores.rum)))
    threads.append(threading.Thread(target=run_pump, args=(PUMPS["orange"], coctel.orange, sensores.orange)))
    threads.append(threading.Thread(target=run_pump, args=(PUMPS["lime"], coctel.lime, sensores.lime)))
    threads.append(threading.Thread(target=run_pump, args=(PUMPS["sweetener"], coctel.sweetener, sensores.sweetener)))

    for t in threads:
        t.start()
    for t in threads:
        t.join()
