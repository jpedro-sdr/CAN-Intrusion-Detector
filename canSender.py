import can

def sendMessages():
  with can.Bus(interface='socketcan', channel='can0', bitrate=500000) as bus:
    with open('candump_new.txt', 'r') as messages_to_send:
      for message_line in messages_to_send:
        message_splited = message_line.split()
        timestamp = message_splited[0]
        message = message_splited[2]
        message_data = message.split('#')
        id = message_data[0]
        data = message_data[1]

        msg = can.Message(
          arbitration_id=id,
          data=bytes.fromhex(f'{data[:2]} {data[2:]}')
        )
        try:
          bus.send(msg)
          print(f"Message sent on {bus.channel_info}")
        except can.CanError:
          print("Message NOT sent")

if __name__ == "__main__":
  sendMessages()
