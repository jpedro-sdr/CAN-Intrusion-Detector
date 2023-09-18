import requests
import json
from checkMessage import checkMsg
from checkMessage import set_message_last_timestamp


def print_red(text):
    print("\033[91m" + text + "\033[0m")

def dockerPrediction(messages: list):
    docker_server_url = "http://172.22.202.88:8081/predict"

    try:
        data = json.dumps({"instances": messages})  # Send the list of messages inside "instances"
        headers = {"Content-Type": "application/json"}  # Set the header to indicate that you are sending JSON


        payload = json.dumps({"instances": messages})
        response = requests.post(docker_server_url, data=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            process_predictions(result, messages)
        else:
            print("Error in HTTP request:", response)
    except Exception as e:
        print("Error in HTTP request:", str(e))

def process_predictions(predictions: list, messages: list):
    #predictions = predictions
    # print(predictions)
    for instance_dict, prediction in zip(messages, predictions):
        print("Prediction:", dict(prediction))
        if prediction['scores'][1] > 0.50:
            id_value = instance_dict["ID"]
            dlc_value = instance_dict["DATA"]
            message = f"Dangerous message ID: {id_value} - DLC: {dlc_value} - Score: {prediction['scores'][1]}\n"
            print_red(message)  # Imprime a mensagem em vermelho
            with open("ReceivedMessages/DangerousMessages.txt", "a") as file:
                file.write(message)
