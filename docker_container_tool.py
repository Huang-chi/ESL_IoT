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
    parser.add_argument("-d", "--delete", type=str, default="NULL", help='delete all container')
    # parser.add_argument("-n", "--network", type=str, default="NULL", help='copy the network')

    args = parser.parse_args()

    if args.delete != "NULL":
        print("------------Start delete images------------------")
        if args.delete == "all":
            print("------------delete all images------------------")
            delete_all_container()
        else :
            print("------------delete "+args.delete+"-------------------")
            delete_container(args.delete)
        show_all_container()

    category = ""
    container_name = ""
    mangement_container_name = "container_M_0"


    if args.category != "NULL":
        args.category = args.category.upper()
        category = args.category
        if category == "DNN" or category == "BC" :
            print("Create container category "+args.category)
            container_name = get_new_container_name(category)
            modify_dockerfile_port(container_name, category)

        elif category == "IOT":
            print("Create container category "+args.category)
            container_name = get_new_container_name(category)
            modify_dockerfile_port(container_name, category)
            
        else:
            print("Don't suppert the caregory :"+category)

        try:
            if category == "IOT" or args.dockerfile != "NULL" :
                print("Build dockerfile's named "+args.dockerfile)
                build_container(args.dockerfile)
                print("Run mangement container's named "+args.dockerfile)
                mangement_container_name = run_container(mangement_container_name, args.dockerfile)
    
            elif category != "IOT" or args.dockerfile != "NULL" :
                build_container(args.dockerfile)
                run_main_container(mangement_container_name, container_name, args.dockerfile)
            else:
                print("No find the category or no find the image. ")
        except:
            print("Creating container is failed. ")
