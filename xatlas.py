
#!/usr/bin/env python
# encoding: utf-8

import argparse
import os
import re


#################################wrapper for xatlas####################################



def xatlascommand(args, log, exePath):

	slurmVar = ''
	if args.slurm == True:
		slurmVar = "srun -N {} -c {}".format(args.node, args.core, args.thread) 

	
	log.info("Execute command :{} {} -r {} -i {}  -c {} -t {} -s {} -p {}".format(slurmVar , exePath, args.genome_ref, args.bam, args.bed, args.thread, args.sample, args.vcf))
	os.system(" {} {} -r {}  -i {}  -c {} -t {} -s {} -p {}".format(slurmVar, exePath, args.genome_ref, args.bam, args.bed, args.thread, args.sample, args.vcf))
	log.debug(" sample argument is required")





	
	

 	

 	return 0

 	###xatlas =/usr/local/bin/xatlas


