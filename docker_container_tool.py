import subprocess
import csv
import sys
import os
import argparse

sys.path.append(os.path.join(os.path.dirname(__file__),'lib'))

from modify_dockerfile import modify_dockerfile_port
from create_container_name import get_new_container_name


CONTAINER_WORD_LENGTH = 12

def create_container(mangement_container_name,container_name,docker_version_name = "mytomcat2"):
    try:
        result = subprocess.check_call("sudo docker run -d --name "+container_name+" --net=container:"+mangement_container_name+" -it "+docker_version_name+" /bin/bash", shell=True)
        print(result == 0)
    except subprocess.CalledProcessError as err:
        print("Command Error")


def delete_all_conttoller():
    try:
        subprocess.check_call("sudo docker stop $(sudo docker ps -a -q)", shell=True)
        subprocess.check_call("sudo docker rm $(sudo docker ps -a -q)", shell=True)

    except subprocess.CalledProcessError as err:
        print("Command Error")

def delete_conttoller(container_name):
    try:
        subprocess.check_call("sudo docker stop "+container_name, shell=True)
        subprocess.check_call("sudo docker rm "+container_name, shell=True)

    except subprocess.CalledProcessError as err:
        print("Command Error")

def show_all_container():
    try:
        subprocess.check_call("sudo docker ps -a", shell=True)

    except subprocess.CalledProcessError as err:
        print("Command Error")

def stop_container(container_name):
    try:
        subprocess.check_call("sudo docker stop "+container_name, shell=True)

    except subprocess.CalledProcessError as err:
        print("Command Error")


def build_container(image_name):
    try:
        subprocess.check_call("sudo docker build -t "+image_name +" . --no-cache", shell=True)
    except subprocess.CalledProcessError as err:
        print("Command Error")

def run_container(mangement_container_name,docker_version_name = "mytomcat1"):
    
    try:
        subprocess.check_call("sudo docker run -d --name "+mangement_container_name+" -it "+docker_version_name+" /bin/bash", shell=True)
    except subprocess.CalledProcessError as err:
        print("Command Error")
    return mangement_container_name

def update_momery_container(mangement_container_name,size):
        
    try:
        subprocess.check_call("docker update -m" + size +" --memory-swap -1 "+ mangement_container_name+, shell=True)
    except subprocess.CalledProcessError as err:
        print("Command Error")

def update_cpu_container(mangement_container_name,size):
        
    try:
        subprocess.check_call("docker update -m" + size +" "+ mangement_container_name", shell=True)
    except subprocess.CalledProcessError as err:
        print("Command Error")

# def get_new_container_name(category):
#     with open('container_port.csv', newline='') as csvfile:
#         # Read CSV to dictionary
#         rows = csv.DictReader(csvfile)
#         temp = []
#         for row in rows:
#             print(row)
#             temp.append(row['container_name'])
#         data_length = len(temp)

#         # print(data_length)
#         # print(temp[data_length-1][CONTAINER_WORD_LENGTH:])

#         container_name = "container_"+category+"_"+str(int(temp[data_length-1][CONTAINER_WORD_LENGTH:])+1)
#         print(container_name)
#         return container_name


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Please enter images name: ')
    parser.add_argument("-t", "--dockerfile", type=str, default="NULL", help='Build dockerfile')
    parser.add_argument("-c", "--category", type=str, default="NULL", help='Chooses category')
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
        build_container(args.docke