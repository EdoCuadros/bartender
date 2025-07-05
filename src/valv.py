import RPi.GPIO as GPIO
import time
import os
from simple_pid import PID

IN1 = 22


# La entrada de ambas funciones debe ser un vector con los pines de IN1, IN2, EN -> [IN1, IN2, EN]

def init_pump(IN1):
    """
    Inicializa los pines para uso del puente H.
    Input:
    - _GPIO: Tupla que contiene los pines de Input1 y Enable de la bomba.
    """
    try:
        GPIO.setmode(GPIO.BCM)  # Configuración de pines de microprocesador
    except:
        print("Falta importar las librerías")
    # Configuración de pines como salidas
    GPIO.setup(IN1, GPIO.OUT)


def run_pump(IN1: int, setpoint: int, sensor):
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
    pwm.start(0)

    try:
        while True:
            level = sensor.range    # [mm]
            output = pid(level)
            pwm.ChangeDuty(output)

            if abs(level - setpoint) < 2:
                break

            time.sleep(0.1)
    finally:
        pwm.stop()
        GPIO.cleanup()
        