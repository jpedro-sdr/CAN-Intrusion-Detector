import os
import asyncio
from typing import Dict
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value

def print_red(text):
    print("\033[91m" + text + "\033[0m")

def predict_tabular_classification_sample(
    project: str,
    endpoint_id: str,
    instances: Dict,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    client_options = {"api_endpoint": api_endpoint}
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    #print("aqui2",instances)
    for instance_dict in instances:
        instance = json_format.ParseDict(instance_dict, Value())
        instances = [instance]
        parameters_dict = {}
        #print("aqui3", instances)
        parameters = json_format.ParseDict(parameters_dict, Value())
        endpoint = client.endpoint_path(project=project, location=location, endpoint=endpoint_id)
        #print(endpoint)
        try:
            #print("Entrou no try")
            #print(endpoint)
            #print(parameters)
            #print(instances)
            response = client.predict(endpoint=endpoint, instances=instances, parameters=parameters)
        except Exception as e:
            print(e)        
        print(" deployed_model_id:", response.deployed_model_id)
        predictions = response.predictions
        for prediction in predictions:
            print(" prediction:", dict(prediction))
            if prediction['scores'][1] > 0.50:
                id_value = instance_dict["ID"]
                dlc_value = instance_dict["DLC"]
                message = f"Dangerous message ID: {id_value} - DLC: {dlc_value} - Classe 1 - Score: {prediction['scores'][1]}\n"
                print_red(message)  # Imprime a mensagem em vermelho
                with open("DangerousMessages.txt", "a") as file:
                    file.write(message)
                
                  
