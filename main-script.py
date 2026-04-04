#!/usr/bin/env python3

import my_function

def main():
    input_name = input("Enter your name: ")
    my_function.greeting(input_name)

# set the environment for this script
# is it main(), or is this a module being called by something else?
if __name__ == '__main__':
    main()
