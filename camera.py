from picamera import PiCamera
from time import sleep

def getPicture():
    camera = PiCamera()
    camera.start_preview()
    camera.capture('/home/pi/Desktop/image.jpg')
    sleep(10)
    camera.stop_preview()