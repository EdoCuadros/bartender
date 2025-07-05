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
from recipe_config import DRINKS, INGREDIENT_STATUS
from sensores import getLevel, select_channel, init_sensors
from sensarTemp import getTemp
from valv import init_pump, run_pump
from dispenser import dispense

if __name__ == "__main__":

    
    while True:
        init_sensors()
        _estado = leerEstado()
        if _estado.estado == 'pedido' and _estado.coctel:
            coctel = DRINKS[_estado.coctel]
            dispense(coctel)
        


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
