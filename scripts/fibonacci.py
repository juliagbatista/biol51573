#!/usr/bin/env python3

#import packages in the very top of the script
import argparse 

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


#parse the arguments
args = parser.parse_args()

# prompt the user for a position in the Fibonacci sequence
#position = input("Please enter a position in the Fibonacci sequence:")

#initialize two integers
a,b = 0,1 #a=0 and b=1

#loop
#for i in range(int(position)):
 #   a,b = b, a+b

#fibonacci_number = a

#loop

for i in range(int(args.position)):
    a,b = b, a+b

fibonacci_number = a

if args.verbose:
    print(f"The fibonacci number for {args.position} is {fibonacci_number}")
else: 
    print(fibonacci_number)





