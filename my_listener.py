import can
import re
import os
import threading
from predictor import predict_tabular_classification
from dockerPredictor import dockerPrediction

class MyListener(can.Listener):
    def __init__(self):
        super().__init__()
        self.processed_ids = set()  # Conjunto para manter o registro das IDs processadas
        self.message_buffer = []  # Lista para acumular mensagens
        self.previous_message_data = None  # Armazenar os dados da mensagem anterior
        self.lock = threading.Lock()

    def on_message_received(self, msg):
        message_data = self.extract_message_data(msg)
        if message_data:
            if message_data != self.previous_message_data:
                self.process_message_data(message_data)
                self.previous_message_data = message_data

    def extract_message_data(self, msg):
        #print(msg)
        regex_pattern = r'ID:\s+([0-9A-Fa-f]+)\s+.*?\s+DL:\s+(\d+)\s+(.*?)$'
        match = re.search(regex_pattern, str(msg))
        timestamp_match = re.search(r'Timestamp: (\d+\.\d+)', str(msg))
        #print(timestamp_match)
        timestamp = ""
        if timestamp_match:
            timestamp = float(timestamp_match.group(1))
            #print("TimeStamp:", timestamp)
        if match:
            id_value = match.group(1)
            dlc_value = int(match.group(2))
            data_bytes_hex = match.group(3).split()

            if len(data_bytes_hex) >= dlc_value:
                data_bytes_hex = data_bytes_hex[:dlc_value]
                data_hex = ''.join(data_bytes_hex)
                formatted_data_dlc = f"{dlc_value:4d} {data_hex}"
                return {"ID": id_value, "DLC": formatted_data_dlc, "Timestamp": timestamp}
        return None

    def process_message_data(self, message_data):
        id_value = message_data["ID"]
        formatted_data_dlc = message_data["DLC"]
        timestamp = message_data["Timestamp"]
        message_string = f"Mensagem recebida - ID {str(int(id_value)).zfill(4)} - DLC {formatted_data_dlc}"
        print(message_string)
        with open("ReceivedMessages/ReceivedMessages4.txt", "a") as file:
            file.write(message_string + "\n")

        self.processed_ids.add(id_value)
            #timestamp ="2023‑09‑13 11:45:30.005"
            # Check if the message is safe
        is_safe = checkMsg(id_value, message_data, timestamp)
        set_message_last_timestamp(id_value, timestamp)

        if is_safe:
            self.message_buffer.append({'ID': id_value, 'DATA': formatted_data_dlc})

            if len(self.message_buffer) >= 5:
                self.make_batch_prediction()
        else:
            with open("ReceivedMessages/DangerousMessages.txt", "a") as file:
                message = f"Dangerous message ID: {id_value} - DLC: {dlc_value} - Timestamp: {timestamp} - Score: 1\n"
                file.write(message_data)

    def make_batch_prediction(self):
        if self.message_buffer:
            try:
                predict_thread = threading.Thread(
                    target=self.call_predict,
                    args=(self.message_buffer,),
                    daemon=True
                )
                predict_thread.start()
            except Exception as e:
                print(e)

            self.message_buffer = []  # Limpa o buffer após o envio em lote

    def call_predict(self, message_buffer):
        with self.lock:
            try:
                '''predict_tabular_classification(
                    project=os.environ["PROJECT_ID"],
                    endpoint_id=os.environ["ENDPOINT_ID"],
                    instances=message_buffer
                )'''
                dockerPrediction(message_buffer)  # Chame sua função predict_with_docker aqui
            except Exception as e:
                print(e)

    def finalize(self):
        # Enviar mensagens restantes mesmo que não atinjam 50
        if self.message_buffer:
            self.make_batch_prediction()
