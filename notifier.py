import threading
import can

class Notifier(can.Listener):
    def __init__(self, bus, listeners, timeout=1.0):
        super().__init__()
        self.bus = bus
        self.listeners = listeners
        self.timeout = timeout
        self.running = False
        self.thread = threading.Thread(target=self._run)

    def _run(self):
        self.running = True
        while self.running:
            message = self.bus.recv(self.timeout)
            if message is not None:
                for listener in self.listeners:
                    listener.on_message_received(message)

    def on_message_received(self, msg):
        pass

    def start(self):
        self.running = True
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()
