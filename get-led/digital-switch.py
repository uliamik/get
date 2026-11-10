import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
button = 13

GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

state = 0
GPIO.output(led, state)
button_pressed = False

try:
    while True:
        if GPIO.input(button) == 1 and not button_pressed:
            state = 1 - state
            GPIO.output(led, state)
            button_pressed = True
        elif GPIO.input(button) == 0:
            button_pressed = False
        time.sleep(0.05)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()