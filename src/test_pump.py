import RPi.GPIO as GPIO
import time
import os

IN1 = 23
IN2 = 24
EN = 18

GPIO.setmode(GPIO.BCM)  # Configuración de pines de microprocesador

# Configuración de pines como salidas
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(EN, GPIO.OUT)

# Optional: PWM on EN for speed control
pwm = GPIO.PWM(EN, 1000)  # 1 kHz
duty_cycle = 100
pwm.start(duty_cycle)  # 100% duty cycle (full power)

try:
    print("Turning pump ON for 5 seconds...")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)   # One direction
    time.sleep(5)

    print("Turning pump OFF")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)  # optional, stops PWM
except KeyboardInterrupt:
    pass
finally:
    pwm.stop()
    GPIO.cleanup()