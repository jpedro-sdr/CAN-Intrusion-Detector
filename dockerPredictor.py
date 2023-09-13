import requests
import json
from checkMessage import checkMsg
from checkMessage import set_message_last_timestamp
def dockerPrediction(messages: list):
    docker_server_url = "http://172.20.36.224:8081/predict"

    try:
        data = json.dumps({"instances": messages})  # Send the list of messages inside "instances"
        headers = {"Content-Type": "application/json"}  # Set the header to indicate that you are sending JSON

        # Loop through the messages to check each one
        for message in messages:
            #print("gg",message)
            id_value = message["ID"]
            message_data = message["DLC"]
            timestamp = message["Timestamp"]
            #print("time",timestamp)
            #print(message_data)
            #timestamp ="2023‑09‑13 11:45:30.005"
            # Check if the message is safe
            is_safe = checkMsg(id_value, message_data, timestamp)
            set_message_last_timestamp(id_value, timestamp)
            #print("aqui", is_safe)
            if  not is_safe:
                # Only make the request if the message is safe
                payload = json.dumps({"instances": [{"ID": id_value, "DATA": message_data}]})
                #print("Payload:", payload)  # Adicione este log para verificar o payload enviado
                response = requests.post(docker_server_url, data=payload, headers=headers)
                #print("a")
                if response.status_code == 200:
                    result = response.json()
                    #print("aa", result)
                    process_predictions(result)
                else:
                    print("11Error in HTTP request:", response)
            else:
                print("Not making a request for a dangerous message.")
    except Exception as e:
        print("Error in HTTP request:", str(e))

def process_predictions(predictions: list):
    #print("pp")
    #predictions = predictions
    print(predictions)
    for prediction in zip(predictions):
        print("prediction:", dict(prediction))
        if prediction['scores'][1] > 0.50:
       #     id_value = instance_dict["ID"]
        #    dlc_value = instance_dict["DLC"]
             message = f"Dangerous message  Classe 1 - Score: {prediction['scores'][1]}\n"
             print_red(message)  # Imprime a mensagem em vermelho
             with open("ReceivedMessages/DangerousMessages.txt", "a") as file:
                file.write(message)
