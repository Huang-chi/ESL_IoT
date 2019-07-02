#!/usr/bin/env python python3

import socket

def listen_outside_network(port):

#     HOST = '172.17.0.2'
    HOST = '192.168.112.133'
    PORT = port


    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind((HOST , PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr )
            data = conn.recv(1024)
        #     break
        s.close
    print('Received', repr(data))
    return repr(data)
