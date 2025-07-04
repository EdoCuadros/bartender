from dataclasses import asdict
import sys
import os
import requests
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
import RPi.GPIO
import time
from interface import(
    ESTADO,
    IOT,
    leerEstado,
    reset,
    registrarIOT,
    resultadoPedido
)
from recipe_config import DRINKS
from sensarNivel import getLevel, select_channel, init_sensors
from sensarTemp import getTemp
from valv import init_pump, run_pump


"""
def handle_drink_request(drink_number):
    pass
    #dispenser.dispense(drink_number, DRINKS)
"""


if __name__ == "__main__":

    while True:

        _estado = leerEstado()
        if _estado.estado == 'pedido':
            coctel = _estado.coctel
        
        match coctel:
            case "Daiquiri":
                # TODO:funcion para coctel 1
                pass
            case "Rum Punch":
                # TODO:funcion para coctel 2
                pass
            case "Mai Tai":
                # TODO: funcion para coctel 3
                pass
            case "Cuban Sunset":
                # TODO: funcion para coctel 4
                pass
            case "Tropical Sour":
                # TODO: funcion para coctel 5
                pass
            case _:
                time.sleep(5)
        


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
