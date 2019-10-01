#!/usr/bin/env python3

import socket
import sys
import socketserver
import json
import threading
import time

from pandas import read_csv
from pandas import DataFrame
from pandas import concat

HOST = '127.0.0.1'
PORT = 6000

#!/usr/bin/env python3


def socket_connect(message):
    message = transfer_to_json(message)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        RxData = message.encode('utf-8')
        size = sys.getsizeof(RxData)
        print(size)
        print(RxData)
        if RxData:
            s.sendall(str(size).encode('utf-8'))
            time.sleep(0.5)
            s.sendall(RxData)
        s.close()

def transfer_to_json(message):
    if type(message) is list:
        jmsg1 = json.dumps(message)
        return jmsg1

if __name__ == "__main__":
    datasets = read_csv('Residential-Profiles_Plus_AVG_SORT.csv', header=0, index_col=0)
    title_list = list(datasets)
    dict = {}

    for title in title_list:
        value = datasets[title]
        data_len = len(value)
        print(data_len)
        dict[title] = list(value)
        # print(dict[title])

    for title in title_list:
        print(dict["H-30"][0:1])
    # socket_connect(dict["H-30"])