import requests
import json
from checkMessage import checkMsg

def dockerPredictor(messages: list):
    docker_server_url = "http://192.168.0.3:8081/predict"

    try:
        data = json.dumps({"instances": messages})  # Send the list of messages inside "instances"
        headers = {"Content-Type": "application/json"}  # Set the header to indicate that you are sending JSON

        # Loop through the messages to check each one
        for message in messages:
            id_value = message["ID"]
            message_data = message["data"]
            timestamp = message["timestamp"]

            # Check if the message is safe
            is_safe = checkMsg(id_value, message_data, timestamp)

            if is_safe:
                # Only make the request if the message is safe
                response = requests.post(docker_server_url, data=data, headers=headers)

                if response.status_code == 200:
                    result = response.json()
                    process_predictions(result)
                else:
                    print("Error in HTTP request:", response.status_code)
            else:
                print("Not making a request for a dangerous message.")
    except Exception as e:
        print("Error in HTTP request:", str(e))

def process_predictions(predictions: list):
    for prediction in predictions:
        if prediction['scores'][1] > 0.50:
            id_value = prediction["ID"]
            dlc_value = prediction["DLC"]
            message = f"Dangerous message ID: {id_value} - DLC: {dlc_value} - Classe 1 - Score: {prediction['scores'][1]}\n"
            print_red(message)
            with open("ReceivedMessages/DangerousMessages.txt", "a") as file:
                file.write(message)
