from azure.cosmos import exceptions, CosmosClient, PartitionKey
import os

url = 'https://komato.documents.azure.com:443/'
key = '6yGKuFvOQrU7WsKGonsdBuhpKTHB1ZC4U8VEXeuvEnfKJGFh2CKlsynBO7nPcztp97juCNAnDcKQxIfFJOHHYg=='
try:
    client = CosmosClient(url, credential=key)
    database_name = 'komatodb'
    database = client.get_database_client(database_name)
    container_name = 'komatoGrow'
    container = database.get_container_client(container_name)
except ValueError as e:
    raise Exception('Invalid json: {}'.format(e)) from None

# Enumerate the returned items
import json
for item in container.query_items(
        query='SELECT * FROM c',
        enable_cross_partition_query=True):
    print(json.dumps(item, indent=True))