#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
from socker_listen_for_outside import *
from socker_listen_for_inner import *

values = ""

while True:
    if(sys.argv[0] != None):
        values = listen_inner_network(sys.argv[0])
    else:
    # serverrr(sys.argv[0])
        values = listen_outside_network(8002)
print('put data into DNN model')
print(values)