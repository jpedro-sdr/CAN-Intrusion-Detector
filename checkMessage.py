import re
import datetime
from messages import messages

def print_red(text):
    print('\033[91m' + text + '\033[0m')

def get_message_by_id(target_id):
    for message in messages:
        if message["id"] == target_id:
            return message
    return None

def checkDataFormat(data, expected_message):
    # mask = re.escape(expected_message["format"])
    mask = expected_message["format"]
    mask = mask.replace("#", "[0-1]")
    regularExpression = f"^{mask}$"
    # print(re.match(regularExpression, data))
    return re.match(regularExpression, data) is not None

# def extractSignalFromMessage(data, expected_message):
#     mask = expected_message["format"]
#     extracted_signals = []
#     lastCharacter = ''
#     nextString = ''
#     for i, character in enumerate(mask):
#         if character == "#":
#             if lastCharacter == "#" or lastCharacter == '':
#                 nextString += data[i]
#             elif lastCharacter == "0":
#                 if nextString != '':
#                     extracted_signals.append(nextString)
#                 nextString = ''
#                 nextString += data[i]
#         lastCharacter = character
#     extracted_signals.append(nextString)
#     return extracted_signals

def newExtractSignalFromMessage(data, expected_message):
    match = re.search(expected_message["pattern"], data)
    if match is None:
        return None 
    matches = list(match.groups())
    # print(matches)
    return matches

def checkSignalRange(signalValue, expected_signal):
    if signalValue < expected_signal["min"] or signalValue > expected_signal["max"]:
        return False
    return True

def getSignalValue(signal, expected_signal):
    value = signal * expected_signal["scale"] + expected_signal["offset"]
    return value

def stringBinToInt(string):
    # print(string, type(string))
    return int(string, 2)

def stringToHex(string):
    return int(string, 16)

def checkDataRange(data, expected_message):
    # print(expected_message)
    # print(data)
    signals = newExtractSignalFromMessage(data, expected_message)
    # print(signals)
    for signal in signals:
        signal_index = signals.index(signal)
        expected_signal = expected_message["signals"][signal_index]
        # print(signal, type(signal), 'antes do stringBinToInt')
        signal = stringBinToInt(signal)
        value = getSignalValue(signal, expected_signal)
        # print(signal, 'signal')
        if not checkSignalRange(value, expected_signal):
            # print(value, 'value')
            # print(f'Value of signal {expected_signal["signal"]} is out of range. Invasion detected')
            return False
    return True
        # print(f'{expected_signal["signal"]}: {value}')

def checkPeriod(timestamp, id):
    expected_message = get_message_by_id(id)
    if expected_message is None:
        return False
    evalueated_message_timestamp = datetime.datetime.fromtimestamp(timestamp)
    
     
    if expected_message.get("last_message_timestamp") is None:
        # print(f'First message of message with id ${id}.')
        return True
    last_message_timestamp = expected_message["last_message_timestamp"]
    last_message_timestamp = datetime.datetime.fromtimestamp(last_message_timestamp)
    delta = evalueated_message_timestamp - last_message_timestamp
    milliseconds = delta.total_seconds() * 1000
    msg_period = expected_message["period"]
    # print(f'Delta of message with id ${id} is {milliseconds} milliseconds. Allowed: {expected_message["period"]} milliseconds.')

    if milliseconds/msg_period < 0.95: # 5% of tolerance
        print(f'[Out of period] Period of message with id ${id} is lower than allowed. Allowed: {expected_message["period"]}, Received: {milliseconds}')
        return False
    return True


def set_message_last_timestamp(id, timestamp):
    expected_message = get_message_by_id(id)
    if expected_message is None:
        print(f'Message with id ${id} is not in the allowed list, so the timestamp cannot be updated.')
        return False
    expected_message["last_message_timestamp"] = timestamp
    return True


# (1694027572.059435) can0 360#8AD800C3A0000000

def checkMsg(id, data, timestamp):
    id = id.upper()
    data = data.upper()
    # data = data.lstrip()
    if len(data) < 2:
        print_red(f'Data of message with id {id} is not allowed. Invasion detected')
        return False
        # Remova o primeiro caractere que não seja espaço
    # data = " ".join(data.split())
    # for i, char in enumerate(data):
    #     if char != ' ':
    #         data = data[:i] + data[i+1:]
    #         break
    # id = id.lstrip('0')
    # print('Data before transform', data)
    first_part_data = data[:2]
    second_part_data = data[2:]
    second_part_data = second_part_data.replace('\n', '')
    data = f'{second_part_data}{first_part_data}'
    data_hex = stringToHex(data)
    #print("passou")
    data_binary = bin(data_hex)
    data_binary = data_binary[2:]
    data = data_binary.zfill(16)[::-1]
    # print(data_binary, type(data_binary), 'data_binary', data)
    expected_message = get_message_by_id(id)
    if expected_message is None:
        print_red(f'Message with id {id} is not allowed in the message list. Invasion detected')
        return False
    isFormatAllowed = checkDataFormat(data, expected_message)
    if not isFormatAllowed:
        print_red(f'Format of message with id {id} is not allowed. Invasion detected')
        return False
    areSignalsInRange = checkDataRange(data, expected_message)
    if not areSignalsInRange:
        print_red(f'Values of signals of message with id {id} are out of range. Invasion detected')
        return False
    isPeriodAllowed = checkPeriod(timestamp, id)
    if not isPeriodAllowed:
        print_red(f'Timestamp of message with id {id} is not allowed. Invasion detected')
        return False
    return True
    



if __name__ == '__main__':
    # print(messages)
    cntt = 0
    with open('candump_new.txt', 'r') as f:
       lines = f.readlines()
       for line in lines:
           line = line.split(' ')
           id = line[2].split('#')[0]
           data = line[2].split('#')[1]
           timestamp = line[0].split('(')[1].split(')')[0]
           # print(timestamp, 'timestamp')
           timestamp = float(timestamp)
           isMsgValid = checkMsg(id, data, timestamp)
           set_message_last_timestamp(id, timestamp)
           if not isMsgValid:
                cntt += 1
                # print(line, type(line), 'line')
                with open('invalid_msgs4.txt', 'a') as f2:
                    f2.write(' '.join(line))
    print('Wrong cases: ', cntt)            
    
