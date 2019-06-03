from search_container_port import check_no_same_port
from search_container_port import write_new_data

def modify_dockerfile_port(container_name):
    fopen = open("./example/Dockerfile",'r+')
    w_str = ""
    port = str(check_no_same_port())
    write_new_data(container_name,port)

    print(port)
    for line in fopen.readlines():
        if "port" in line:
            print("Before modify"+line)
            print("After modify"+line.replace("port",port))
            line = line.replace("port",port)
        w_str += line

    wopen = open("Dockerfile",'w')
    wopen.write(w_str)
    fopen.close()
    wopen.close()
    return True

# if __name__ == "__main__":
#     modify_dockerfile_port("test")