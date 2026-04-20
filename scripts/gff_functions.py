#!/usr/bin/env python3

#------ function to open and read the genome FASTA file
def read_fasta(fasta_file):
    print(f"Reading FASTA file: {fasta_file}")

    genome_sequence = ""

    # open the FASTA file and read each line
    with open(fasta_file, "r") as f:
        for line in f:
            # skip the first header line (starts with '>')
            if line.startswith(">"):
                continue
            # strip the newline character from each line and add to genome_sequence
            genome_sequence += line.strip()

    print(f"Done reading FASTA file. Genome length: {len(genome_sequence)} bp")
    return genome_sequence


#------ function to read and parse the GFF3 file
def read_gff(gff_file, genome_sequence):
    print(f"Reading GFF file: {gff_file}")

    features = []

    # open the GFF3 file and read each line
    with open(gff_file, "r") as f:
        for line in f:
            # skip comment lines
            if line.startswith("#"):
                continue
            # strip newline and split columns by tab
            cols = line.strip().split("\t")
            # make sure we have a full GFF line (9 columns)
            if len(cols) < 9:
                continue

            # extract begin and end coordinates (cols 4 and 5, 1-based in GFF)
            begin = int(cols[3]) - 1   # convert to 0-based index
            end = int(cols[4])         # end is inclusive in GFF, exclusive in Python slicing

            # extract the sequence from the genome using the coordinates
            extracted_sequence = genome_sequence[begin:end]

            # extract the sequence ID from the last column (after "ID=")
            attributes = cols[8]
            seq_id = ""
            for attribute in attributes.split(";"):
                if attribute.startswith("ID="):
                    seq_id = attribute.replace("ID=", "")
                    break

            print(f"  Extracted feature: {seq_id} ({len(extracted_sequence)} bp)")
            features.append((seq_id, extracted_sequence))

    print(f"Done reading GFF file. Total features extracted: {len(features)}")
    return features


#------ function to write extracted sequences to a FASTA output file
def write_output(features, output_file="covid_genes.fasta"):
    print(f"Writing output to: {output_file}")

    with open(output_file, "w") as out:
        for seq_id, sequence in features:
            # write in FASTA format: header line then sequence
            out.write(f">{seq_id}\n")
            out.write(f"{sequence}\n")

    print(f"Done writing output file: {output_file}")


# set the environment for this script
# is it main(), or is this a module being called by something else?
if __name__ == '__main__':
