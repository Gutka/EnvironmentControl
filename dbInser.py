from azure.cosmos import exceptions, CosmosClient, PartitionKey
from datetime import datetime
from json import dumps
import os


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
                    "temp": 20.5,
                    "humidity": 60.5
                }
                        ],
            "lightSensor":True,
            "date": datetime.now().isoformat()
})