import subprocess
import csv
import sys
import os
import argparse

sys.path.append(os.path.join(os.path.dirname(__file__),'lib'))

from modify_dockerfile import modify_dockerfile_port
from create_container_name import get_new_container_name
from docker_tool import *


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Please enter images name: ')
    parser.add_argument("-t", "--dockerfile", type=str, default="NULL", help='Build dockerfile')
    parser.add_argument("-c", "--category", type=str, default="NULL", help='Chooses category')
    parser.add_argument("-m", "--memory", type=str, default="NULL", help='Craeate memory size')
    args = parser.parse_args()

    category = ""

    if args.category != "NULL":
        args.category = args.category.upper()
        if args.category == "DNN" or args.category == "BC":
            print("Create container category "+args.category)
            category = args.category
        else:
            print("Don't suppert the caregory :"+args.category)

    container_name = get_new_container_name(category)
    modify_dockerfile_port(container_name, category)

    mangement_container_name = "container_1"

    

    if args.dockerfile != "NULL" :
        print("Build dockerfile's named "+args.dockerfile)
        build_container(args.dockerfile)
        print("Run mangement container's named "+args.dockerfile)
        mangement_container_name = run_container(mangement_container_name, args.dockerfile)
    
    create_container(mangement_container_name, container_name, args.dockerfile)
