import can
import re
import os
from predictor import predict_tabular_classification_sample

class MyListener(can.Listener):
    def __init__(self):
        super().__init__()
        self.processed_ids = set()  # Conjunto para manter o registro das IDs processadas

    def on_message_received(self, msg):
        regex_pattern = r'ID:\s+([0-9A-Fa-f]+)\s+.*?\s+DL:\s+(\d+)\s+(.*?)$'
        #regex_pattern = r'Timestamp:\s+(\d+)\s+ID:\s+([0-9A-Fa-f]+)\s+DL:\s+(\d+)\s+(.*?)$'
        #regex_pattern = r'Timestamp:\s+([\d.]+)\s+ID:\s+([0-9A-Fa-f]+)\s+[A-Za-z]+\s+DL:\s+(\d+)\s+([0-9a-f\s]+)\s+Channel:\s+([^\s]+)'
        match = re.search(regex_pattern, str(msg))
        print(msg)
        if match:
            #timestamp = match.group(1)
            id_value = match.group(1)
            dlc_value = int(match.group(2))
            data_bytes_hex = match.group(3).split()
            
            if len(data_bytes_hex) >= dlc_value:
                data_bytes_hex = data_bytes_hex[:dlc_value]
                data_hex = ''.join(data_bytes_hex)
                formatted_data_dlc = f"{dlc_value:4d} {data_hex}"
                data_from_message = {"ID": id_value, "DLC": formatted_data_dlc}
                #print("AquiSTR", str(int(id_value)).zfill(4))
            if id_value not in self.processed_ids or True:
                message_string = f"Mensagem recebida - ID {str(int(id_value)).zfill(4)} - DLC {formatted_data_dlc}"
                print(message_string)
                # Salvar a mensagem no arquivo "ReceivedMessages.txt"
                with open("ReceivedMessages4.txt", "a") as file:
                    file.write(message_string + "\n")
                
                data_from_message = {"ID": str(int(id_value)).zfill(4), "DLC": formatted_data_dlc}
                try:
                    predict_tabular_classification_sample(
                        project=os.environ["PROJECT_ID"],
                        endpoint_id=os.environ["ENDPOINT_ID"],
                        instances=[data_from_message]
                    )
                except Exception as e:
                    print(e)
               
                # Adicione a ID da mensagem ao conjunto de IDs processadas
                self.processed_ids.add(id_value)

        else:
            print("Erro no processamento da mensagem.")
