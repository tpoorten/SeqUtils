#!/usr/bin/env python

import sys, random, itertools
import HTSeq

fraction = float(sys.argv[1])
in1 = iter( HTSeq.FastqReader( sys.argv[2] ) )
out1 = open( sys.argv[3], "w" )

for read1 in in1:
	if random.random() < fraction:
		read1.write_to_fastq_file( out1 )


out1.close()

