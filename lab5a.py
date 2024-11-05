#!/usr/bin/env python3
# Author ID: twangmo12

def read_file_string(file_name):
    # Takes file_name as a string for a file name, returns its entire contents as a string
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    # Takes file_name as a string for a file name,
    # returns its entire contents as a list of lines without new-line characters
    with open(file_name, 'r') as f:
        return [line.strip() for line in f]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
