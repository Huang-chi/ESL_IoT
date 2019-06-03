#!/usr/bin/env python python3

import socket
from docker_container_tool import create_container
from modify_dockerfile import modify_dockerfile_port

def serverrr(port):

    HOST = '127.0.0.1'
    PORT = port


    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind((HOST , PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr )
            data = conn.recv(1024)
    print('Received', repr(data))

    with open('container_port.csv', newline='') as csvfile:
        # Read CSV to dictionary
        rows = csv.DictReader(csvfile)
        temp = []
        for row in rows:
            print(row)
            temp.append(row['container_name'])
        len = len(temp)
        container_name = temp[len-1][:len-2]+str(int(temp[len-1][len-2:])+1)
        modify_dockerfile_port(container_name)
        create_container(container_name)

        csvfile.close()