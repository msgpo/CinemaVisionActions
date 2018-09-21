import sys
from websocket import create_connection
import json
import time

URL_TEMPLATE = "{scheme}://{host}:{port}{path}"


socket_host = "192.168.0.41" #this should be the ip address of the mycroft device on the local network
socket_port = 8181 #this port should match the client port


def send_message(message, host=socket_host, port=socket_port, path="/core", scheme="ws"):
    payload = json.dumps({
        "type": "recognizer_loop:utterance",
        "context": "",
        "data": {
            "utterances": [message]
        }
    })
    url = URL_TEMPLATE.format(scheme=scheme, host=host, port=str(port), path=path)
    ws = create_connection(url)
    ws.send(payload)
    ws.close()


# mute Command
# send_message('PleaseBeSilent')
# time.sleep(1)

send_message('turn the wall lights on silently')
time.sleep(2)

send_message('set the wall lights to orange silently')
time.sleep(15)

# un-mute Command
# send_message('YouCanSpeakNow')
# print('no longer silent')


