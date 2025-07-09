from dataclasses import dataclass
from enum import Enum
from typing import Optional, Literal
import requests
from dataclasses import asdict

API = 'https://3okai9k1ec.execute-api.us-east-1.amazonaws.com/prod/Coctelera'
headers = {'Authorization': 'API_COCTELERA_HASH_KEY' }

PUMPS:dict[str, int] = {
    "rum": 26,
    "sweetener": 17,
    "orange": 27,
    "lime": 22
    #"out": 0
}

class EstadoEnum(str, Enum):
    IDLE = 'IDLE'
    LLAVE = 'LLAVE'
    PEDIDO = 'PEDIDO'
    ERROR = 'ERROR'
    FIN = 'FIN'

class CoctelEnum(str, Enum):
    CLASSIC_DAIQUIRI = 'Daiquiri'
    RUM_PUNCH = 'Rum Punch'
    MAI_TAI = 'Mai Tai'
    CUBAN_SUNSET = 'Cuban Sunset'
    TROPICAL_SOUR = 'Tropical Sour'

class DataCoctel:
    def __init__(self, info: dict[str, int]):
        self.rum = info["rum"]
        self.orange = info["orange"]
        self.lime = info["lime"]
        self.sweetener = info["sweetener"]
    rum: int
    orange: int
    lime: int
    sweetener: int

@dataclass
class ESTADO:
    def __init__(self,data):
        self.estado =  data['estado'] 
        self.coctel =  data['coctel'] if 'coctel' in data else None
        self.llave =  data['llave'] if 'llave' in data else None
        self.error =  data['error'] if 'error' in data else None

    estado: EstadoEnum
    coctel: Optional[CoctelEnum]
    llave: Optional[str]
    error: Optional[str]

@dataclass
class IOT:
    def __init__(
        self,
        bomb1: int,
        bomb2: int,
        bomb3: int,
        bomb4: int,
        bombOut: int,
        motor: int,
        encoder: int,
        nivel1: int,
        nivel2: int,
        nivel3: int,
        nivel4: int,
        temp1: float,
        temp2: float,
        temp3: float,
        temp4: float,
        tempOut: float
    ):
        self.bomb1 = bomb1
        self.bomb2 = bomb2
        self.bomb3 = bomb3
        self.bomb4 = bomb4
        self.bombOut = bombOut
        self.motor = motor
        self.encoder = encoder
        self.nivel1 = nivel1
        self.nivel2 = nivel2
        self.nivel3 = nivel3
        self.nivel4 = nivel4
        self.temp1 = temp1
        self.temp2 = temp2
        self.temp3 = temp3
        self.temp4 = temp4
        self.tempOut = tempOut

    bomb1: int
    bomb2: int
    bomb3: int
    bomb4: int
    bombOut: int
    motor: int
    encoder: int    # Queda pendiente
    nivel1: int
    nivel2: int
    nivel3: int
    nivel4: int
    temp1: float
    temp2: float
    temp3: float
    temp4: float
    tempOut: float

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

