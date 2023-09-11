import os
import asyncio
from typing import List, Dict
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value
import threading

def print_red(text):
    print("\033[91m" + text + "\033[0m")

def predict_tabular_classification(
    project: str,
    endpoint_id: str,
    instances: List[Dict],
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    def _predict_thread():
        client_options = {"api_endpoint": api_endpoint}
        client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
        instances_proto = [json_format.ParseDict(instance_dict, Value()) for instance_dict in instances]
        parameters_dict = {}
        parameters = json_format.ParseDict(parameters_dict, Value())
        endpoint = client.endpoint_path(project=project, location=location, endpoint=endpoint_id)
        try:
            response = client.predict(endpoint=endpoint, instances=instances_proto, parameters=parameters)
        except Exception as e:
            print(e)
        print(" deployed_model_id:", response.deployed_model_id)
        predictions = response.predictions
        for instance_dict, prediction in zip(instances, predictions):
            print(" prediction:", dict(prediction))
            if prediction['scores'][1] > 0.50:
                id_value = instance_dict["ID"]
                dlc_value = instance_dict["DLC"]
                message = f"Dangerous message ID: {id_value} - DLC: {dlc_value} - Classe 1 - Score: {prediction['scores'][1]}\n"
                print_red(message)  # Imprime a mensagem em vermelho
                with open("ReceivedMessages/DangerousMessages.txt", "a") as file:
                    file.write(message)

    thread = threading.Thread(target=_predict_thread)
    thread.start()
    thread.join()
