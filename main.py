import os
import can
import threading
from my_listener import MyListener
from notifier import Notifier
# from predictor import predict_tabular_classification
from dockerPredictor import dockerPrediction

os.environ["ENDPOINT_ID"] = "539941573098471424"
os.environ["PROJECT_ID"] = "792014674767"
os.environ["INPUT_DATA_FILE"] = "INPUT-JSON"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "serviceAccount.json"
os.environ['GRPC_DNS_RESOLVER'] = 'native'

def main():
    print("Conexão com o barramento estabelecida.")
    with can.Bus(receive_own_messages=True) as bus:
        print_listener = MyListener()
        custom_notifier = Notifier(bus, [print_listener])
        custom_notifier.start()

        try:
            while True:
                pass
        except KeyboardInterrupt:
            custom_notifier.stop()

if __name__ == "__main__":
    main()
