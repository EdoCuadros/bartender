import RPi.GPIO as GPIO
import time
from interface import ESTADO, PUMPS, DataCoctel
from valv import run_pump
import threading

# TODO: Escribir la función para dispensar bebidas

def dispense(coctel: DataCoctel, s):
    threads = []

    threads.append(threading.Thread(target=run_pump, args=(PUMPS["rum"], coctel.rum, s)))
    threads.append(threading.Thread(target=run_pump, args=(PUMPS["orange"], coctel.orange, s)))
    threads.append(threading.Thread(target=run_pump, args=(PUMPS["lime"], coctel.lime, s)))
    threads.append(threading.Thread(target=run_pump, args=(PUMPS["sweetener"], coctel.sweetener, s)))

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # TODO: Actualiza estados de los ingredientes