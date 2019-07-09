#!/usr/bin/env python3

import socket
import sys
import socketserver
import json
import threading

HOST = '127.0.0.1'
PORT = 6000

#!/usr/bin/env python3


def socket_connect(message):
    message = transfer_to_json(message)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        RxData = message.encode('utf-8')
        print(RxData)
        if RxData:
            s.send(RxData)
        s.close()

def transfer_to_json(message):
    if type(message) is list:
        jmsg1 = json.dumps(message)
        return jmsg1


msg1 = [{'src':"zj", 'dst':"zjdst"}]
socket_connect(msg1)