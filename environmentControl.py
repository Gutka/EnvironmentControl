from azure.cosmos import exceptions, CosmosClient, PartitionKey
from datetime import datetime
from json import dumps
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import os


DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
LIGHT_PIN = 17

def GetTemp():
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	return ['{:.2f}'.format(temperature), '{:.2f}'.format(humidity)]

def GetLight():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LIGHT_PIN, GPIO.IN)
    if GPIO.input(LIGHT_PIN) == 0:
        return True
    else:
        return False
    return


url = 'https://komato.documents.azure.com:443/'
key = 'uNqR2I7O5gd7cpxEDyKFZZ7VuJgF0dgJZZBj37WxPNnhvVcB9YMYICiK5d47BMe8zPrTNBAnetVPrGJwiYaEfg=='
try:
    client = CosmosClient(url, credential=key)
    database_name = 'komatodb'
    database = client.get_database_client(database_name)
    container_name = 'komatoGrow'
    container = database.get_container_client(container_name)
except ValueError as e:
    raise Exception('Invalid json: {}'.format(e)) from None


container.upsert_item({
            "runID": 1,
            "tempSensor": [
                 {
                    "temp": GetTemp()[0],
                    "humidity": GetTemp()[1]
                }
                        ],
            "lightSensor":GetLight(),
            "date": datetime.now().isoformat()
})
