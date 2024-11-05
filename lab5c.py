#!/usr/bin/env python3
# Author ID: twangmo12

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        return int(number1) + int(number2)
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except (FileNotFoundError, IOError):
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                        # Should output: 15
    print(add('10', 5))                      # Should output: 15
    print(add('abc', 5))                     # Should output: 'error: could not add numbers'
    print(read_file('seneca2.txt'))          # Should output: List of lines from 'seneca2.txt'
    print(read_file('file10000.txt'))        # Should output: 'error: could not read file'
