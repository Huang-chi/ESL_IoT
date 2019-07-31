#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
from socker_listen_for_outside import *
from socker_listen_for_inner import *

values = ""

while True:
    if(sys.argv[1] == "in"):
        print("1")
        values = listen_inner_network(sys.argv[0])
    elif(sys.argv[1] == "out"):
    # serverrr(sys.argv[0])
        values = listen_outside_network(8002)
    else:
        print("Don't input tag( in or out ) not yet")
print('put data into DNN model')
print(values)