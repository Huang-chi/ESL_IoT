import csv
DEFINE_PORT = 6000

def check_no_same_port(new_port = None):
    with open('container_port.csv', newline='') as csvfile:
        # Read CSV to dictionary
        rows = csv.DictReader(csvfile)

        temp = None

        for row in rows:
            print("Check....")
            if row['port'] == str(new_port):
                return None
            print(row)
            temp = row['port']
            print(type(temp))

        csvfile.close()
        if temp is None:
            return DEFINE_PORT

        elif new_port is None:
            return int(temp) + 1
        
        return new_port

def write_new_data(container_name,port):
    f = open('container_port.csv', 'a', newline='')
    writer = f.write(container_name+","+port+'\n')
    
if __name__ == "__main__":
    port = check_no_same_port()
    print(port)
    write_new_data("test",str(port))