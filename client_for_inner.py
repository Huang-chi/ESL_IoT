#!/usr/bin/env python3

import socket
import sys

HOST = '172.17.0.2'
PORT = 6000

def socket_connect(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        RxData = data.encode('utf-8')
        print(RxData)
        if RxData:
            s.send(RxData)
        s.close()

socket_connect("3513")