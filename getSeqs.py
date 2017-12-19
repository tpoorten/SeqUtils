#!/usr/bin/env python
# Tom Poorten, December 2017, UC Davis
# get subset of fasta records and make new fasta file

from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser(description='creates a new fasta file with only specified records, which are provided in a text file')
parser.add_argument('-i', help='input fasta', dest='fastaIn',required=True)
parser.add_argument('-k', help='records to keep; given from a text file', dest='fileIn',required=True)
parser.add_argument('-o', help='output fasta', dest='fastaOut',required=True)
args = parser.parse_args()

fastaIn = args.fastaIn
fileIn = args.fileIn
fastaOut = args.fastaOut

file = open(fileIn)
recsToKeep = []
for line in file:
    recsToKeep.append(line.rstrip())
file.close()

record_dict = SeqIO.index(fastaIn, "fasta")

with open(fastaOut, "w") as output_handle:
    for i in recsToKeep:
        SeqIO.write(record_dict[i], output_handle, "fasta")
