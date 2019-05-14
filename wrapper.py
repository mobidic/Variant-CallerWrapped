#!/usr/bin/env python
# encoding: utf-8

import argparse
import os
import re
import logging # logging messages
import sys
import freebayes
from freebayes import *
import xatlas
from xatlas import *
import octopus
from octopus import *


################################# wrapper ####################################



def checkArguments(args, log):

	"""@summary = returns a log.error when you do not use the parameters listed"""

	

 	
	if not args.variant_caller or not args.genome_ref or not args.bam  or not args.bed or not args.vcf:
		log.error("necessary pre-requisite arguments")
		sys.exit()

	
	if args.genome_ref:
		if not os.path.isfile(args.genome_ref): 
 		
 			log.error("it does not exist file corresponding to the reference genome")
 			sys.exit()

 		if not os.access(args.genome_ref, os.R_OK):
 			log.error("permission to read the reference genome file is not accorded")
 			sys.exit()

	   
 	if args.bam:
 		if not os.path.isfile(args.bam): 
 		
 			log.error("it does not exist file corresponding to the bam")

 			sys.exit()

 		if not os.access(args.bam, os.R_OK):
 			log.error("permission to read the bam file is not accorded")
 			sys.exit()


 	if args.bed:
 		if not os.path.isfile(args.bed):
 			log.error("it does not exist file corresponding to the target regions")
 			sys.exit()

 		if not os.access(args.bed, os.R_OK):
 			log.error("permission to read the target regions file is not accorded")
 			sys.exit()

	

def wichPath(variant_caller):
    
    """@summary: Returns the path to the software from the PATH environment variable.
    @param software: [str] Name of the software.
    @return: [str/None] The path of the software or None if it is not found."""
    
    callerPath = None
    PATH = os.environ.get('PATH')
    #print(os.pathsep)
    #for current_folder in reversed(PATH.split(os.pathsep)):  # Reverse PATh elements to kept only the first valid folder
    for currentFolder in PATH.split(os.pathsep):
        print(currentFolder)
        evalPath = os.path.join(currentFolder, variant_caller)
        #print(eval_path)
        if os.path.exists(evalPath):
            callerPath = evalPath
        
 	
	return callerPath	





def desiredVariantCaller(args, log, exePath):

	"""@summary = allows to run the command for each variantcaller"""
	
	if args.variant_caller == 'freebayes':
		freebayes.freecommand(args, log, exePath)
	
		
	elif args.variant_caller == 'xatlas':
		xatlas.xatlascommand(args, log, exePath)

	elif args.variant_caller == 'octopus': 
		octopus.octocommand(args,log, exePath)

	else:
		log.error("could not found the variantcaller")
		sys.exit()

################################################################################
#
# CLASS
#
################################################################################
class LoggerAction(argparse.Action):
    """
    @summary: Manages logger level parameters (The value "INFO" becomes logging.info and so on).
    """
    def __call__(self, parser, namespace, values, option_string=None):
        log_level = None
        if values == "DEBUG":
            log_level = logging.DEBUG
        elif values == "INFO":
            log_level = logging.INFO
        elif values == "WARNING":
            log_level = logging.WARNING
        elif values == "ERROR":
            log_level = logging.ERROR
        
        setattr(namespace, self.dest, log_level)





if __name__ == "__main__":
	#manage parametters

	parser = argparse.ArgumentParser(description = "wrapper for variant caller")
	
	parser.add_argument('-vc', '--variant_caller', help= 'the path to the variantcaller installation folder')
	parser.add_argument('--vc_path', help='the required option when you do not find the path of variantcaller')
	parser.add_argument('-g', '--genome_ref', help= 'the reference genome file')
	parser.add_argument('-b', '--bam', help= 'the bam file')
	parser.add_argument('-v', '--vcf',  help= 'the output vcf file')
	#parser.add_argument('-p', '--prefix', help = 'output prefix')
	parser.add_argument('-s', '--sample', help ='Sample name to use in the output VCF file')
	

	parser.add_argument('--slurm', help = 'Required option when you want to run multiple jobs' action='store_true')

	parser.add_argument('-N', '--node', help = 'the number of nodes used', default = 1, type = int)
	parser.add_argument('-c', '--core', help = 'the number of cores used', default = 1, type = int)
	parser.add_argument('-t', '--thread', default = 1, help = 'the number of threads used', type = int)



	parser.add_argument('-be', '--bed', default = '/usr/local/share/refData/intervals/MedExome_2019.bed ',help= ' the bed file containing target regions')
	

	
	# parser.add_argument('-z', help = 'anonyme')
	# parser.add_argument('-F',  help= 'Enable SNP filter for single-strandedness')
	# parser.add_argument('-P', help = 'Read alignment file and process records in separate threads', type = int)



	parser.add_argument('-l', '--logging-level', default="DEBUG", choices=["DEBUG", "INFO", "WARNING", "ERROR"], action=LoggerAction, help='The logger level. [Default: %(default)s]')


	args = parser.parse_args()

	


	"""if args.thread:
		print(args.thread * 2)

	if args.variantcaller:
		print(args.variantcaller)


	"""
		

	logging.basicConfig(format='%(asctime)s - %(name)s [%(levelname)s] %(message)s')
	log = logging.getLogger("Wrapper")
	log.setLevel(args.logging_level)
	log.info("Wrapper started")
	log.info("Command: " + " ".join(sys.argv))
	#log.debug("DEBUG level message")
	#log.info("INFO level message")
	#log.warning("WARNING level message")
	#log.error("ERROR level message")
	
	checkArguments(args, log)
	Warning(args, log)

	wichPath(args.variant_caller)

	
	
	log.debug(args.variant_caller)
	#print wichPath(args.variant_caller)
	exePath = None

	if not args.vc_path:

		exePath = wichPath(args.variant_caller)
		#print exePath
		
		
	if exePath is None:
		if args.vc_path:
			
			exePath = args.vc_path
			if not os.path.isfile(exePath):
				log.error(" the file corresponding to your variantcaller does not exists")
				sys.exit()
			if not os.access(exePath, os.X_OK):
				log.error("permission to run the variantcaller is not accorded")
				sys.exit()
	
		else: 
			log.error("Could not find path for you variant caller use --vc-path option to specify the correct path")
			sys.exit()
	
	

	

	log.debug(exePath)


	desiredVariantCaller(args, log, exePath)
	
	
	
	
	




