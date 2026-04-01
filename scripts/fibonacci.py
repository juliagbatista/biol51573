#!/usr/bin/env python3


#import packages in the very top of the script
import argparse 
#------ function to parse the command line arguments
def get_args():
    ###------ accept and parse command line arguments
    #create an argument parser object 
    parser = argparse.ArgumentParser(description="This script calculates the number at a given position \
                                    in the Fibonacci sequence")

    #add a positional argument, in this case, the position in the Fibonacci sequence 
    parser.add_argument("position",help="Position in the Fibonacci sequence",type=int)

    # an optional argument for verbose ouput or not
    ## if 'store_true', this means assign 'TRUE' if the optional argument is specified
    #on the comand line, so the default for 'store_true' is actually false 

    parser.add_argument("-v", "--verbose",help="Print verbose otput", action='store_true')


    #parse the arguments and return in two steps
    args = parser.parse_args()
    return args
    #or, parse the arguments and return in one step
    #return parser.parse_args()


#------- function to calculate Fibonacci number 
def fib():
    # prompt the user for a position in the Fibonacci sequence
    #position = input("Please enter a position in the Fibonacci sequence:")

    #initialize two integers
    a,b = 0,1 #a=0 and b=1

    #loop

    for i in range(int(beyonce.position)):
        a,b = b, a+b

    fibonacci_number = a
    return fibonacci_number

#----- function to print the Fibonacci number at the given position, with an optional verbose output
def print_output(output):
    if beyonce.verbose:
        print(f"The fibonacci number for {beyonce.position} is {output}")
    else: 
        print(fibnum)
    

#------ define the main() function to call the other functions in the correct order
def main():
    fibnum = fib()
    print_output(fibnum)
    #this print statement will not print variables that are local to fib()
    #print(a , b, fibonacci_number)

#------ calling get_args() happens out here on its own
beyonce = get_args()

# to creat function we add in the end of the script, we will do 3 (import, function definition, and then the main code block)
# set the environment for this script 
# is this main (i.e., a standalone Python script), or
# is this a python module being called by another script

if __name__ == '__main__': 
    main()



