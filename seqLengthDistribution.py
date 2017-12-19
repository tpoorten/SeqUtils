#!/usr/bin/env python

## Tom Poorten, April 2016, UC Davis

## Usage: ./seqLengthDistribution.py fileName.fasta
## Output: fileName.pdf with distribution of lengths
## Use in a loop like so: for f in ../fastaFiles/*.fasta; do echo "File is '$f'"; ../seqLengthDistribution.py $f; done

# magic command for ipython plotting
# %matplotlib

import sys
from Bio import SeqIO
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib as mpl
import seaborn as sns
sns.set(color_codes=True)

fileIn = sys.argv[1]
targetName = fileIn.split("/")[-1]
targetName = targetName.split(".")[1]

## Get Sequence lengths in fasta file
sizes = [len(rec) for rec in SeqIO.parse(fileIn, "fasta")]
#len(sizes), min(sizes), max(sizes)
#np.median(sizes)

## Make plot
figSizes = plt.figure()
sns.distplot(sizes);
plt.title("%s: %i Sequences\nLengths: %i to %i; Median: %i" \
            % (targetName,len(sizes),min(sizes),max(sizes), np.median(sizes)))
plt.xlabel("Sequence length (bp)")
plt.ylabel("Count")
plt.axvline(np.median(sizes), color='k', linestyle='-'); # median
plt.axvline(np.mean(sizes), color='r', linestyle='-'); #
plt.axvline((np.mean(sizes) - np.std(sizes)), color='r', linestyle='--'); #
plt.axvline( (np.mean(sizes) - (2*np.std(sizes))), color='r', linestyle='-.'); #
#plt.show()
figSizes.savefig("%s.pdf" % (targetName), bbox_inches='tight')
plt.close()
#
