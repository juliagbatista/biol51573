#!/usr/bin/env python3

# verify that sequence lengths in covid_genes.fasta and match the expected lengths from covid_genes.gff3
# Expected length formula: (end - start) + 1

gff_file  = "/Users/quantgen/Documents/classes/project/data/files/data/covid_genome/covid_genes.gff3"
fasta_file = "/Users/quantgen/Documents/classes/biol51573/scripts/covid_genes.fasta"

# Read expected lengths from GFF3 
expected = {}   # { sequence_id : expected_length }

with open(gff_file) as f:
    for line in f:
        if line.startswith("#") or line.strip() == "":
            continue
        cols = line.strip().split("\t")
        start  = int(cols[3])
        end    = int(cols[4])
        length = (end - start) + 1   

        # Extract ID= from the attributes column (col 9)
        attributes = cols[8]
        seq_id = None
        for attr in attributes.split(";"):
            if attr.startswith("ID="):
                seq_id = attr[3:]
                break

        if seq_id:
            expected[seq_id] = length

# Read actual lengths from FASTA
actual = {}   # { sequence_id : actual_length }

with open(fasta_file) as f:
    current_id  = None
    current_seq = ""
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            if current_id:
                actual[current_id] = len(current_seq)
            current_id  = line[1:]   # remove the >
            current_seq = ""
        else:
            current_seq += line
    if current_id:   # save the last sequence
        actual[current_id] = len(current_seq)

# Compare expected and actual lengths and print results
print(f"{'Sequence ID':<30} {'Expected':>10} {'Actual':>10} {'Match':>8}")
print("-" * 62)

all_correct = True

for seq_id in sorted(expected):
    exp_len = expected[seq_id]
    if seq_id in actual:
        act_len = actual[seq_id]
        match   = "YES" if exp_len == act_len else "NO"
        if exp_len != act_len:
            all_correct = False
    else:
        act_len = "MISSING"
        match   = "MISSING"
        all_correct = False
    print(f"{seq_id:<30} {exp_len:>10} {str(act_len):>10} {match:>8}")

print("-" * 62)
if all_correct:
    print("\n All sequence lengths are correct")
else:
    print("\n Some sequences have incorrect lengths. Check above.")
