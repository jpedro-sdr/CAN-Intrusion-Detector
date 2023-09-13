import requests
import json

def predict_with_docker(messages: list):
    docker_server_url = "http://192.168.0.7:8081/predict"

    try:
        data = json.dumps({"instances": messages})  # Envie a lista de mensagens dentro de "instances"
        headers = {"Content-Type": "application/json"}  # Defina o cabeçalho para indicar que você está enviando JSON

        response = requests.post(docker_server_url, data=data, headers=headers)  # Faça uma solicitação POST

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

def main():
    # Exemplo de lista de mensagens contendo apenas "ID" e "DLC"
    messages = [
        {"ID": 123, "DLC": 112233},
        {"ID": 234, "DLC": 223344},
    ]

    predict_with_docker(messages)

if __name__ == "__main__":
    main()
