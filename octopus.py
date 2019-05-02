import argparse
import os
import re


#################################wrapper for octopus####################################

def octoprocess(args):
	variantcaller = args.variantcaller
	genomeref = args.genomeref
	bam = args.bam
	output = args.vcf

	print("{} -R {} -I {} -v {}".format(variantcaller, genomeref, bam, output))


def octocommand(args,log):
	variantcaller = args.variantcaller
	genomeref = args.genomeref
	bam = args.bam
	output = args.vcf

 	log.info("Execute command : {} -f {} {} -v {}".format(variantcaller, genomeref, bam, output))
	cmd = os.system("{} -f {} {} -v {}".format(variantcaller, genomeref, bam, output))
	#print(cmd)

 	return 0







if __name__ == "__main__":
	#manage parametters

	parser = argparse.ArgumentParser(description = "wrapper for variant caller")
	
	parser.add_argument('-p', '--path', default = "/softs/octopus/bin/octopus", help= 'the path to the freebayes installation folder')
	parser.add_argument('-R', '--genomeref', default = '/usr/local/share/refData/genome/hg19/hg19.fa', help= 'reference genome.fasta')
	parser.add_argument('-I', '--bam', help= 'bam file')
	parser.add_argument('-v', '--vcf',  help= 'the output vcf file')

	parser.add_argument('-c', '--bed', help= ' bed file containing target regions')
	#parser.add_argument('-t', '--thread', help = 'number of threads used', type = int)

	args = parser.parse_args()

	"""if args.thread:
		print(args.thread * 2)

	if args.variantcaller:
		print(args.variantcaller)
	"""

	octoprocess(args)
	#octocommand(args,log)
