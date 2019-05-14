import subprocess


def create_controller(controller_name,docker_version_name = "mytomcat"):
    try:
        result = subprocess.check_call("sudo docker run -d --name "+controller_name+" --net=container:container1 -it "+docker_version_name+" /bin/bash", shell=True)
        print(result == 0)
    except subprocess.CalledProcessError as err:
        print("Command Error")

def delete_all_conttoller():
    try:
        subprocess.check_call("sudo docker stop $(sudo docker ps -a -q)", shell=True)
        subprocess.check_call("sudo docker rm $(sudo docker ps -a -q)", shell=True)

    except subprocess.CalledProcessError as err:
        print("Command Error")

def delete_conttoller(controller_name):
    try:
        subprocess.check_call("sudo docker stop "+controller_name, shell=True)
        subprocess.check_call("sudo docker rm "+controller_name, shell=True)

    except subprocess.CalledProcessError as err:
        print("Command Error")

def show_all_controller():
    try:
        subprocess.check_call("sudo docker ps -a", shell=True)

    except subprocess.CalledProcessError as err:
        print("Command Error")

def stop_controller(controller_name):
    try:
        subprocess.check_call("sudo docker stop "+controller_name, shell=True)

    except subprocess.CalledProcessError as err:
        print("Command Error")


if __name__ = '__mian__':
# create_controller("test2")
# delete_conttoller("test2")
# show_all_controller()