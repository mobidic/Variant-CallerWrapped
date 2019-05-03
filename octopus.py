import argparse
import os
import re


#################################wrapper for octopus####################################


def octocommand(args,log):
	variantcaller = args.variantcaller
	genomeref = args.genomeref
	bam = args.bam

	bed = args.bed
	
 	log.info("Execute command : {} -R {} - I {} -t {} ".format(variantcaller, genomeref, bam, bed))
	os.system("{} -R {} -I {} -t {} ".format(variantcaller, genomeref, bam, bed))
	#print(cmd)

 	return 0

 	### path = /softs/octopus/bin/octopus


	