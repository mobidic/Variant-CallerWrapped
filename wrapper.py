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

	variantcaller = args.variant_caller
	genomeref= args.genomeref
	bam = args.bam
	output=args.vcf

 	
	if not variantcaller or not genomeref or not bam or not output:
		log.error("necessary pre-requisite arguments")
		sys.exit()
	
	if genomeref:
		if not os.path.isfile(genomeref): 
 		
 			log.error(genomeref, "does not exists")
	   
 	if bam:
 		if not os.path.isfile(bam): 
 		
 			print(bam, "does not exists")

 	"""if variantcaller:
 		if not os.path.isfile(variantcaller):
 			#print(variant-caller, "exists")
 		#else:
 			print(variantcaller,"does not exists")
	"""

def Warning(args, log):

	"""@summary = returns a log.warning when you do not use the parameters listed"""

 	bed = args.bed
 	thread = args.thread
 	F= args.F
 	P = args.P
 	z = args.z

 	if not bed or not thread or not z or not F or not P:
 		log.warning("missing arguments but its not necessary")
 		

	

def wichPath(variantcaller):
    
    """@summary: Returns the path to the software from the PATH environment variable.
    @param software: [str] Name of the software.
    @return: [str/None] The path of the software or None if it is not found."""
    
    caller_path = None
    PATH = os.environ.get('PATH')
    for current_folder in reversed(PATH.split(os.pathsep)):  # Reverse PATh elements to kept only the first valid folder
        eval_path = os.path.join(current_folder, variantcaller)
        if os.path.exists(eval_path):
            caller_path = eval_path
	return caller_path	



def desiredVariantCaller(args, log, exePath):

	"""@summary = allows to run the command for each variantcaller"""
	
	if args.variant_caller == 'freebayes':
		freebayes.freecommand(args, log, exePath)
	
		
	elif args.variant_caller == 'xatlas':
		xatlas.xatlascommand(args, log, exePath)

	elif args.variant_caller == 'octopus': #or args.variantcaller == os.path.isfile(args.variantcaller):
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
	
	parser.add_argument('-vc', '--variant-caller', help= 'the path to the variantcaller installation folder')
	parser.add_argument('--vc-path', help='the required option when you do not find the path of variantcaller')
	parser.add_argument('-g', '--genomeref', default = '/usr/local/share/refData/genome/hg19/hg19.fa', help= 'reference genome.fasta')
	parser.add_argument('-b', '--bam', help= 'bam file')
	parser.add_argument('-v', '--vcf',  help= 'the output vcf file')
	parser.add_argument('-p', '--prefix', help = 'output prefix')
	parser.add_argument('-s', '--sample', help ='Sample name to use in the output VCF file')


	parser.add_argument('-be', '--bed', default = '/usr/local/share/refData/intervals/MedExome_2019.bed ',help= ' bed file containing target regions')
	parser.add_argument('-t', '--thread', help = 'number of threads used', type = int)

	
	parser.add_argument('-z', help = 'anonyme')
	parser.add_argument('-F',  help= 'Enable SNP filter for single-strandedness')
	parser.add_argument('-P', help = 'Read alignment file and process records in separate threads', type = int)



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
	ExePath = wichPath(args.variant_caller)
	if ExePath is None:
		if args.vc_path:
			ExePath = args.vc_path
		else: 
			log.error("could not find path for you variant caller use --va -path option to specify the correct path")
			sys.exit()
	
	#wichPath(args.variantcaller)
	
	desiredVariantCaller(args, log, ExePath)




	
	
	
	

