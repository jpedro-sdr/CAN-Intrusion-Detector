import requests
import json
from typing import Dict

def predict_with_docker(messages: list):
    docker_server_url = "http://192.168.0.4:8080/predict"

    try:
        data = json.dumps(messages)
        response = requests.post(docker_server_url, data=data)

        if response.status_code == 200:
            result = response.json()
            process_predictions(result)
        else:
            print("Erro na solicitação HTTP:", response.status_code)
    except Exception as e:
        print("Erro na solicitação HTTP:", str(e))

def process_predictions(predictions: list):
    for prediction in predictions:
        if prediction['scores'][1] > 0.50:
            id_value = prediction["ID"]
            dlc_value = prediction["DLC"]
            message = f"Dangerous message ID: {id_value} - DLC: {dlc_value} - Classe 1 - Score: {prediction['scores'][1]}\n"
            print_red(message)
            with open("ReceivedMessages/DangerousMessages.txt", "a") as file:
                file.write(message)


