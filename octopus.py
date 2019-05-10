#!/usr/bin/env python
# encoding: utf-8

import argparse
import os
import re


#################################wrapper for octopus####################################


def octocommand(args, log, exePath):
	slurmVar = ''
	if args.slurm == True:
		slurmVar = "srun -N {} -c {}".format(args.node, args.core, args.thread) 
		#slurmVar = 'srun -N' + args.node +' -c' + args.thread


	

	log.info("Execute command : {} {} -R {} - I {} -t {} > {}".format(slurmVar, exePath, args.genome_ref, args.bam, args.bed,args.vcf))
	os.system("{} {} -R {} -I {} -t {}  > {}".format(slurmVar, exePath, args.genome_ref, args.bam, args.bed, args.vcf))

	





	
 	
	
 	return 0

 	
	