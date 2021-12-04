import Adafruit_DHT
import time
import RPi.GPIO as GPIO
from datetime import datetime

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
LIGHT_PIN = 17

def GetHum():
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	if humidity is not None and temperature is not None:
		print("Teplota={0:0.1f}°C Vlhkost={1:0.1f}%".format(temperature, humidity))
	else:
		print("Chyba: Nelze načíst data ze senzoru!")
	return

def GetLight():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LIGHT_PIN, GPIO.IN)
    if GPIO.input(LIGHT_PIN) == 0:
        print ("svítí")
    else:
        print ("nesvítí")
    return

while True:
	now = datetime.now();
	current_time = now.strftime("%H:%M:%S");
	print("Current Time=",current_time);
	GetHum();
	GetLight();
	time.sleep(3600);
