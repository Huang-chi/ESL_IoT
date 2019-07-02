#!/usr/bin/env python python3

import socket

def listen_inner_network(port):

    HOST = '127.0.0.1'
    PORT = int(str(port))


    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind((HOST , PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr )
            data = conn.recv(1024)
    print('Received', repr(data))
    return repr(data)
