
#!/usr/bin/env python
# encoding: utf-8

import argparse
import os
import re


#################################wrapper for xatlas####################################

def xatlasprocess(args):
	variantcaller= args.variantcaller
	genomeref = args.genomeref
	bam = args.bam
	output = args.prefix

	print("{} -r {}  -i {} -q {}".format(variantcaller, genomeref, bam, output))


"""def xatlascommande(toto):
	variantcaller= args.variantcaler
	genomeref = args.genomeref
	bam = args.bam
	output = args.vcf
 	cmd = os.system("{} -f {} {} -v {}".format(path, genomeref, bam, output))

 	

 	return cmd

"""

if __name__ == "__main__":
	#manage parametters

	parser = argparse.ArgumentParser(description = "wrapper for variant caller")
	
	parser.add_argument('-p', '--variantcaller', default = "/usr/local/bin/xatlas", help= 'the path to the xatlas installation folder')
	parser.add_argument('-r', '--genomeref', default = '/usr/local/share/refData/genome/hg19/hg19.fa', help= 'reference genome.fasta')
	parser.add_argument('-i', '--bam', help= 'bam file')
	parser.add_argument('-q', '--prefix', help = 'output prefix')

	parser.add_argument('-c', '--bed', help= ' bed file containing target regions')
	parser.add_argument('-t', '--thread', help = 'number of threads used', type = int)
	parser.add_argument('-s', '--sample', help ='Sample name to use in the output VCF file')
	parser.add_argument('-z', help = 'anonyme')
	parser.add_argument('-F',  help= 'Enable SNP filter for single-strandedness')
	parser.add_argument('-P', help = 'Read alignment file and process records in separate threads', type = int)


	args = parser.parse_args()

	"""if args.thread:
		print(args.thread * 2)

	if args.variantcaller:
		print(args.variantcaller)
	"""

	xatlasprocess(args)
	#xatlascommande(args)





	

	
		


