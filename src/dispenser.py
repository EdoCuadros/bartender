import RPi.GPIO as GPIO
import time

PUMPS = {
    "rum": 17,
    "water": 18,
    "drink3": 19,
    "drink_4": 20,
    "out": 21
}

MOTOR_PIN = 23
#TODO: Verify communication protocols for pumps and sensors.
def initialize():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in list(PUMPS.values()) + [MOTOR_PIN]:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

def run_pump(pin, duration):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pin, GPIO.LOW)

def dispense(drink_number, recipes):
    recipe = recipes.get(str(drink_number))
    if not recipe:
        print(f"[!] Unknown drink number: {drink_number}")
        return
    
    print(f"[*] Dispensing drink #{drink_number}")
    for ingredient, duration in recipe.items()
    pin = PUMPS.get(ingredient)
    if pin:
        print(f"    Pumping {ingredient} for {duration}s")
        run_pump(pin,duration)
    
    print(f"    Mixing...")
    GPIO.output(MOTOR_PIN, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(MOTOR_PIN, GPIO.LOW)
    print(f"[✓] Done!\n")