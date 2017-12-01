from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
camera = PiCamera()
camera.vflip = True
camera.hflip = True

while True:
    input_state = GPIO.input(21)
    if input_state == False:
        camera.start_preview()
	print("getting photo")
        sleep(2)
        camera.capture('./came/image.jpg')
        camera.stop_preview()
        os.rename('came','came(new)')
	print('folder has been renamed')
        sleep(0.2)
