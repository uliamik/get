import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
phototransistor = 6

GPIO.setup(led, GPIO.OUT)
GPIO.setup(phototransistor, GPIO.IN)

try:
    while True:
        light_state = GPIO.input(phototransistor)
        led_state = not light_state
        GPIO.output(led, led_state)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()