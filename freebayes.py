#!/usr/bin/env python
# encoding: utf-8

import argparse
import os
import re
import logging # logging messages
import sys


#################################wrapper for freebayes####################################

def freecommand(args, log, exePath):


	slurmVar = ''
	if args.slurm == True:
		slurmVar = "srun -N {} -c {}".format(args.node, args.core, args.thread) 
		#slurmVar = 'srun -N' + args.node +' -c' + args.thread


	
	log.info("Execute command : {} {} -f {} -t {} {} -v {}".format(slurmVar, exePath, args.genome_ref, args.bed, args.bam, args.vcf))
	os.system("{} {} -f {} -t {} {} -v {}".format(slurmVar,exePath, args.genome_ref, args.bed ,args.bam, args.vcf))
	


	return 0


	

 