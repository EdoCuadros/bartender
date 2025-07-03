from dataclasses import asdict
import sys
import os
import requests
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from interface import ESTADO, IOT
from recipe_config import DRINKS


API = 'https://3okai9k1ec.execute-api.us-east-1.amazonaws.com/prod/Coctelera'
headers = {'auth': 'API_COCTELERA_HASH_KEY' }

"""
def handle_drink_request(drink_number):
    pass
    #dispenser.dispense(drink_number, DRINKS)
"""

def leerEstado()->ESTADO:
    response = requests.get(API, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return ESTADO(data['results'])
    else:
        print(f"Error {response.status_code}: {response.text}")

def reset()->ESTADO:
    response = requests.delete(API, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return ESTADO(data['results'])
    else:
        print(f"Error {response.status_code}: {response.text}")

def registrarIOT(info:IOT):
    response = requests.post(API, headers=headers, json=asdict(info))
    if response.status_code == 200:
        print("TODO BIEN")
    else:
        print(f"Error {response.status_code}: {response.text}")

def resultadoPedido(info:ESTADO)->ESTADO:
    response = requests.put(API, headers=headers, json=asdict(info))
    if response.status_code == 200:
        data = response.json()
        return ESTADO(data['results'])
    else:
        print(f"Error {response.status_code}: {response.text}")


if __name__ == "__main__":
    print(reset())

    # TODO: Mandar cada cierto tiempo el estado de los sensores
    # TODO: Cada X tiempo leer el estado, cuando estado = pedido, leer coctel y usar funciones.
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
