import csv

def check_no_same_port(new_port = None):
    with open('controller_port.csv', newline='') as csvfile:
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
            return 6000

        elif new_port is None:
            return int(temp) + 1
        
        return new_port

def write_new_data(controller_name,port):
    f = open('controller_port.csv', 'a', newline='')
    writer = f.write(controller_name+","+port+'\n')
    
if __name__ == "__main__":
    port = check_no_same_port()
    print(port)
    write_new_data("test",str(port))