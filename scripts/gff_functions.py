#!/usr/bin/env python3

# function to open and read the genome FASTA file

## put the file name as an argument to the function so it can be used in main() and called from the command line

fasta_file = "/Users/quantgen/Documents/classes/project/data/files/data/covid_genome/covid.fasta"
gff_file = "/Users/quantgen/Documents/classes/project/data/files/data/covid_genome/covid_genes.gff3"

# function to read FASTA and return the genome sequence 
def read_fasta(fasta_file):
    
    # open the FASTA file and read it line by line
    fasta = open(fasta_file, "r")

    # skip the first header line
    next(fasta)

    # jump the header line and read the rest
    genome_sequence = ""

    for line in fasta:
        # using strip to remove the newline character from each line
        line = line.strip()
        genome_sequence += line

    print(f"Genome length: {len(genome_sequence)} bp")
    return genome_sequence

# function to read the GFF file 
def read_gff(gff_file, genome_sequence):
    
    # open the GFF3 file and read it line by line
    gff = open(gff_file, "r")

    # create an empty dictionary to store sequence_id : sequence pairs
    gene_sequences = {}

    for line in gff:
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
        #list index 8 of columns and split by ";" to get individual attributes, then find the one that starts with "ID=" and extract the sequence ID, where 3: removes the "ID=" prefix from the attribute value
        #the gff file reads starting with 1, but python uses 0-based indexing, so we need to subtract 1 from the start position when slicing the genome sequence
        #so the start of python will be start = gff start - 1, and the end will be gff end (since the end position in GFF is inclusive, we can use it directly for slicing)
        
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

    gff.close()
    print(f"{len(gene_sequences)} features extracted.")
    return gene_sequences


# function to write the extracted sequences to a FASTA file
## takes the gene_sequences dictionary and the output file name as arguments
### writes each sequence in FASTA format: >sequence_id on one line, sequence on the next

def write_output(gene_sequences, output_file):
    print(f"Writing output to: {output_file}")

    # open the output file for writing
    output = open(output_file, "w")

    # loop over each sequence ID and its sequence in the dictionary
    for sequence_id, sequence in gene_sequences.items():
        # write the FASTA header line with the sequence ID
        output.write(f">{sequence_id}\n")
        # write the sequence on the next line
        output.write(f"{sequence}\n")

    output.close()
    print(f"Done writing output file. {len(gene_sequences)} sequences written.")
