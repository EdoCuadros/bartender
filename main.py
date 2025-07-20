from dataclasses import asdict
import random
import sys
import os
import threading
import requests
import busio
import board
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
import RPi.GPIO
import time
from interface import(
    ESTADO,
    IOT,
    CoctelEnum,
    DataCoctel,
    leerEstado,
    reset,
    registrarIOT,
    resultadoPedido
)
from recipe_config import DRINKS, INGREDIENT_STATUS     
from sensores import SensorEnum, Sensores
from sensarTemp import getTemp
from valv import init_pumps, run_pump
from dispenser import dispense

# TODO: Implementar error

def hacerCoctel():
    time.sleep(5)
    print(resultadoPedido(ESTADO({"coctel": "Mai Tai",
                            "estado": "FIN"})))
    
def procesarEstado():
    reset()
    en_proceso = False
    threads1 = []
    while True:
        _estado = leerEstado()
        print(_estado)
        if _estado.estado == "PEDIDO" and _estado.coctel and not en_proceso:
            en_proceso = True
            
            threads1.append(threading.Thread(target=hacerCoctel))
            threads1.append(threading.Thread(target=write_iot_onprocess))
            for t in threads1:
                t.start()
            for t in threads1:
                t.join()

        if _estado.estado == "IDLE":
            en_proceso = False
            for t in threads1:
                t.terminate()
        time.sleep(2)

def iot_random():
    return IOT(random.randint(1,10),
               random.randint(1,10),
               random.randint(1,10),
               random.randint(1,10),
               random.randint(1,10),
               random.randint(1,10),
               random.randint(1,10),
               random.randint(1,10),
               random.randint(1,10),
               random.randint(1,10),
               random.randint(1,10),
               random.randint(1,10),
               random.randint(1,10),
               random.randint(1,10),
               random.randint(1,10),
               random.randint(1,10))

def write_iot():
    while True:
        test = iot_random()
        registrarIOT(test)
        time.sleep(60)

def write_iot_onprocess():
    while True:
        test = iot_random()
        registrarIOT(test)
        time.sleep(2)
    
 
if __name__ == "__main__":

    threads = []

    threads.append(threading.Thread(target=procesarEstado))
    threads.append(threading.Thread(target=write_iot))

    for t in threads:
        t.start()
    for t in threads:
        t.join()

def main2():
    # Se inician sensores y valvulas
    print("Iniciando sensores")
    i2c = busio.I2C(board.SCL, board.SDA)
    sensores = Sensores(i2c)
    init_pumps()

    # TODO: Como se verifica que el vaso esta puesto y esta vacío???
    # Se empieza a leer los estados
    _estado = leerEstado()
    if _estado.estado == "proceso" and _estado.coctel:
        coctel = DRINKS[_estado.coctel]

    # Se verifica que hay suficientes ingredientes para el coctel seleccionado    
    available_rum = sensores.get_level(SensorEnum.rum_sensor)
    available_lime = sensores.get_level(SensorEnum.lime_sensor)
    available_orange = sensores.get_level(SensorEnum.orange_sensor)
    available_sweetener = sensores.get_level(SensorEnum.sweetener_sensor)

    if available_rum < coctel.rum:
        print("No hay suficiente ron")
        # TODO: Que flujo le hacemos a esto?
    if available_lime < coctel.lime:
        print("No hay suficiente limón")
    if available_orange < coctel.orange:
        print("No hay suficiente naranja")
    if available_sweetener < coctel.sweetener:
        print("No hay suficiente endulzante")
    
    dispense(coctel, sensores)

    while True:
        for channel in SensorEnum:
            level = sensores.get_level(channel)
            print(f"Sensor {channel.name} (channel {channel.value}): {level} mm")
        
        print("-------")
        time.sleep(1)
        

    # TODO: Mandar cada cierto tiempo el estado de los sensores
    # TODO: Implementar interrupción de emergencia
    """
    estado1 = {
        'estado': "ERROR",
        'llave': None,
        'coctel': None,
        'error': "No se pudo :)"
    }

    print(leerEstado())
    print(reset())
    registrarIOT(IOT(3, 5, 1, 3, 1, 2 ,1, 6, 4, 1, 4, 6, 4, 1, 4, 5))
    print(resultadoPedido(ESTADO(estado1)))

    try:



    except KeyboardInterrupt:
        print("\n[!] Shutting down.")
    finally:
        import RPi.GPIO as GPIO
        GPIO.cleanup()
    """
