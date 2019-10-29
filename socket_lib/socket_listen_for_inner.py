#!/usr/bin/env python python3

import socket
import socketserver
import json, types,string

def listen_inner_network(port):

    HOST = '127.0.0.1'
#     PORT = int(str(port))
    PORT = int(port)

    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind((HOST , PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr )
            data = conn.recv(16)
            print(type(repr(data)))

            print('Connected by', addr )
            data = conn.recv(int(repr(data)[2:-1]))

    print('Received', repr(data))
    return repr(data)
