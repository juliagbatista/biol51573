#!/usr/bin/env python3

#exercise 1: Write a Python script called parse_GFF.py that will contain the main() function of your script, call and run it from the command line.
#Use the argparse() module to accept two command line arguments: name of the genome FASTA file and name of the GFF file

#exercise 2: Write a module called gff_functions.py with three functions, read_fasta, read_gff, and write_output

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



# function to open and read the genome FASTA file

## put the file name as an argument to the function so it can be used in main() and called from the command line

fasta_file = "/Users/quantgen/Documents/classes/project/data/files/data/covid_genome/covid.fasta"
gff_file = "/Users/quantgen/Documents/classes/project/data/files/data/covid_genome/covid_genes.gff3"

def read_fasta(fasta_file):
    print(f"Reading FASTA file: {fasta_file}")

    # open the FASTA file and read it line by line
    f = open(fasta_file, "r")

    # skip the first header line
    next(f)

    # initialize genome_sequence as an empty string before adding to it
    genome_sequence = ""

    for line in f:
        # strip the newline character from each line
        line = line.strip()
        genome_sequence += line

    print(f"Done reading FASTA file. Genome length: {len(genome_sequence)} bp")
    return genome_sequence



def read_gff(gff_file, genome_sequence):
    print(f"Reading GFF3 file: {gff_file}")

    # open the GFF3 file and read it line by line
    f = open(gff_file, "r")

    # create an empty dictionary to store sequence_id : sequence pairs
    gene_sequences = {}

    for line in f:
        # skip comment lines that start with '#'
        if line.startswith("#"):
            continue

        # strip the newline character and split the line into columns by tab
        columns = line.strip().split("\t")

        # GFF3 has 9 columns; skip any malformed lines
        if len(columns) < 9:
            continue

        # col 4 = start (1-based), col 5 = end (1-based)
        start = int(columns[3])
        end   = int(columns[4])

        # col 9 = attributes; extract the value that follows "ID="
        attributes = columns[8]
        sequence_id = None
        for attribute in attributes.split(";"):
            if attribute.startswith("ID="):
                sequence_id = attribute[3:]  # remove the "ID=" prefix
                break

        # if no ID was found, skip this feature
        if sequence_id is None:
            continue

        # slice the genome sequence using 0-based indexing (GFF3 is 1-based)
        extracted_sequence = genome_sequence[start - 1:end]

        # store the result in the dictionary
        gene_sequences[sequence_id] = extracted_sequence

        print(f"Extracted sequence for {sequence_id}: {len(extracted_sequence)} bp")

    f.close()
    print(f"Done reading GFF3 file. {len(gene_sequences)} features extracted.")
    return gene_sequences


# function to write the extracted sequences to a FASTA file
## takes the gene_sequences dictionary and the output file name as arguments
### writes each sequence in FASTA format: >sequence_id on one line, sequence on the next

def write_output(gene_sequences, output_file):
    print(f"Writing output to: {output_file}")

    # open the output file for writing
    f = open(output_file, "w")

    # loop over each sequence ID and its sequence in the dictionary
    for sequence_id, sequence in gene_sequences.items():
        # write the FASTA header line with the sequence ID
        f.write(f">{sequence_id}\n")
        # write the sequence on the next line
        f.write(f"{sequence}\n")

    f.close()
    print(f"Done writing output file. {len(gene_sequences)} sequences written.")



# create the main() function to be able to run the script 

def main(): 
    print(f"FASTA file: {args.fasta}")
    print(f"GFF file: {args.gff}")

    # read_fasta() returns the full genome sequence string
    genome_sequence = read_fasta(args.fasta)

    # pass genome_sequence into read_gff() so it can slice out each gene
    gene_sequences = read_gff(args.gff, genome_sequence)

    # write the extracted sequences to covid_genes.fasta in FASTA format
    write_output(gene_sequences, "covid_genes.fasta")

# get the arguments from the command line
args = get_args()

# set the environment for this script
if __name__ == '__main__':
    main()



