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
prev_up = 0
prev_down = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    GPIO.output(leds, dec2bin(num))
    while True:
        curr_up = GPIO.input(button_up)
        curr_down = GPIO.input(button_down)

        if curr_up == 1 and curr_down == 1 and (prev_up == 0 or prev_down == 0):
            num = 255
            GPIO.output(leds, dec2bin(num))
            while GPIO.input(button_up) == 1 or GPIO.input(button_down) == 1:
                time.sleep(0.01)
        elif curr_up == 1 and prev_up == 0 and curr_down == 0:
            num += 1
            if num > 255: num = 0
            GPIO.output(leds, dec2bin(num))
            time.sleep(sleep_time)
        elif curr_down == 1 and prev_down == 0 and curr_up == 0:
            num -= 1
            if num < 0: num = 255
            GPIO.output(leds, dec2bin(num))
            time.sleep(sleep_time)

        prev_up = curr_up
        prev_down = curr_down
        time.sleep(0.01)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()