import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24] 
button_up = 9
button_down = 10

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(button_up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(leds, 0)

num = 0
sleep_time = 0.2

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

up_pressed = False
down_pressed = False

try:
    GPIO.output(leds, dec2bin(num))
    while True:
        if GPIO.input(button_up) == 1 and not up_pressed:
            up_pressed = True
            num += 1
            if num > 255: num = 0
            GPIO.output(leds, dec2bin(num))
            time.sleep(sleep_time)
        elif GPIO.input(button_up) == 0:
            up_pressed = False

        if GPIO.input(button_down) == 1 and not down_pressed:
            down_pressed = True
            num -= 1
            if num < 0: num = 255
            GPIO.output(leds, dec2bin(num))
            time.sleep(sleep_time)
        elif GPIO.input(button_down) == 0:
            down_pressed = False
        time.sleep(0.01)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()