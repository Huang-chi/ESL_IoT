#!/usr/bin/env python python3
import csv
CONTAINER_WORD_LENGTH = 13


def get_new_container_name(category):
    with open('container_port.csv', newline='') as csvfile:
        # Read CSV to dictionary
        rows = csv.DictReader(csvfile)
        temp = []
        for row in rows:
            print(row)
            temp.append(row['container_name'])
        data_length = len(temp)

        print(data_length)
        print(temp[data_length-1][CONTAINER_WORD_LENGTH:])
        print(category)

        container_name = "container_"+category[:2]+"_"+str(int(temp[data_length-1][CONTAINER_WORD_LENGTH:])+1)
        print(container_name)
        return container_name

# if __name__ == '__main__':
#     print(get_new_container_name())
