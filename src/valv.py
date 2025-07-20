import RPi.GPIO as GPIO
import time
import os
from simple_pid import PID

from interface import PUMPS
from sensores import sensorVL53L0X




# La entrada de ambas funciones debe ser un vector con los pines de IN1, IN2, EN -> [IN1, IN2, EN]

def init_pumps():
    """
    Inicializa los pines para uso del puente H.
    Input:
    - _GPIO: Tupla que contiene los pines de Input1 y Enable de la bomba.
    """
    for i in PUMPS.values():
        try:
            GPIO.setmode(GPIO.BCM)  # Configuración de pines de microprocesador
            GPIO.setup(i, GPIO.OUT)
        except:
            print("Falta importar las librerías")
        # Configuración de pines como salidas


      


def run_pump(IN1: int, setpoint: int, sensor : sensorVL53L0X):
    """
    Enciende la bomba para servir los ingredientes.
    Inputs:
    - _GPIO: Tupla que contiene los pines de Input1 y Enable de la bomba.
    - Setpoint: Referencia del controlador. Es el volumen al que debe llegar el controlador (Estado actual - volumen de ingrediente usado).
    - sensor: El objeto del sensor que mide el ingrediente. 
    """
    # Controlador PID
    # TODO: Sintonizar controlador
    pid = PID(1,1,1, setpoint=setpoint)
    pid.output_limits = (0, 100)

    pwm = GPIO.PWM(IN1, 1000)
    pwm.start(100)

    try:
        while True:
            volume = sensor.get_volume    # [mm]
            print(volume)
            output = pid(volume)
            print(output)
            pwm.ChangeDutyCycle(output)

            if abs(volume - setpoint) < 2:
                break

            time.sleep(0.1)
    finally:
        pwm.stop()
        GPIO.cleanup()
        