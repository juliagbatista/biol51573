#!/usr/bin/env python3

#exercise 1: Write a Python script called parse_GFF.py that will contain the main() function of your script, call and run it from the command line.
#Use the argparse() module to accept two command line arguments: name of the genome FASTA file and name of the GFF file


#import packages in the very top of the script
import argparse


# parse the command line arguments
def get_args():
    # create an argument parser object
    parser = argparse.ArgumentParser(description="This script accepts two command line arguments: name of the genome FASTA file and name of the GFF file")

   #add positional argument for the genome FASTA file
    parser.add_argument("fasta", help="Name of the genome FASTA file")
    # add positional argument for the GFF file
    parser.add_argument("gff", help="Name of the GFF file")
    # check the arguments and return them to main()
    args = parser.parse_args()
    return args

# create the main() function to be able to run the script 

def main(): 
    print(f"FASTA file: {args.fasta}")
    print(f"GFF file: {args.gff}")

# get the arguments from the command line
args = get_args()


