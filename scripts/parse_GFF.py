#!/usr/bin/env python3

#exercise 1: Write a Python script called parse_GFF.py that will contain the main() function of your script, call and run it from the command line.
#Use the argparse() module to accept two command line arguments: name of the genome FASTA file and name of the GFF file

#exercise 2: Write a module called gff_functions.py with three functions, read_fasta, read_gff, and write_output

#import packages in the very top of the script
import argparse
import gff_functions


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
    # get the arguments from the command line
    args = get_args()

    # read_fasta() returns the full genome sequence string
    genome_sequence = gff_functions.read_fasta(args.fasta)
    print(genome_sequence)

    # pass genome_sequence into read_gff() so it can slice out each gene
    gene_sequences = gff_functions.read_gff(args.gff, genome_sequence)

    # write the extracted sequences to covid_genes.fasta in FASTA format
    gff_functions.write_output(gene_sequences, "covid_genes.fasta")

# set the environment for this script
if __name__ == '__main__':
    main()



