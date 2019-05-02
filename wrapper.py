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


#################################wrapper####################################



def process(args):
	variantcaller = args.variantcaller
	genomeref = args.genomeref
	bam = args.bam
	output = args.vcf

	print("{} -f {} {} -v {}".format(variantcaller, genomeref, bam, output))


"""def command(args, log):
	variantcaller = args.variantcaller
	genomeref= args.genomeref
	bam = args.bam
	output=args.vcf

	log.info("Execute command : {} -f {} {} -v {}".format(variantcaller, genomeref, bam, output))
	cmd = os.system("{} -f {} {} -v {}".format(variantcaller, genomeref, bam, output))

 	return 0
"""
def Error(args, log):
	variantcaller = args.variantcaller
	genomeref= args.genomeref
	bam = args.bam
	output=args.vcf
 	
	if not variantcaller or not genomeref or not bam or not output:
		log.error("necessary pre-requisite arguments")
	#	print("pre-requisite arguments are good") #je voulais mettre là continuous,mais hors boucle
	#else:
	#	log.error("necessary pre-requisite arguments")

	if genomeref:
		if not os.path.isfile(genomeref): 
 		#	print(genomeref, "exists")
 		#else:
 			log.error(genomeref, "does not exists")
	   
 	if bam:
 		if not os.path.isfile(bam): 
 			#print(bam, "exists")
 		#else:
 			print(bam, "does not exists")

 	if variantcaller:
 		if not os.path.isfile(variantcaller):
 			#print(variant-caller, "exists")
 		#else:
 			print(variantcaller,"does not exists")


def Warning(args, log):
 	bed = args.bed
 	thread = args.thread
 	if not bed or not thread:
 		log.warning("missing arguments are not necessary")
 		log.debug("module arguments must be declared")  ######emplacement pas trop logique.
	


	

def wich(variantcaller):
    
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
        elif values == "CRITICAL":
            log_level = logging.CRITICAL
        setattr(namespace, self.dest, log_level)






if __name__ == "__main__":
	#manage parametters

	parser = argparse.ArgumentParser(description = "wrapper for variant caller")
	
	parser.add_argument('-p', '--variantcaller', help= 'the path to the variantcaller installation folder')
	parser.add_argument('-f', '--genomeref', default = '/usr/local/share/refData/genome/hg19/hg19.fa', help= 'reference genome.fasta')
	parser.add_argument('-b', '--bam', default = '/RS_IURC/data/MobiDL/tests/HC/MiniFastqTest.bam', help= 'bam file')
	parser.add_argument('-v', '--vcf',  help= 'the output vcf file')
	parser.add_argument('-q', '--prefix', help = 'output prefix')


	parser.add_argument('-s', '--bed', help= ' bed file containing target regions')
	parser.add_argument('-t', '--thread', help = 'number of threads used', type = int)

	parser.add_argument('-l', '--logging-level', default="DEBUG", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], action=LoggerAction, help='The logger level. [Default: %(default)s]')


	args = parser.parse_args()

	


	"""if args.thread:
		print(args.thread * 2)

	if args.variantcaller:
		print(args.variantcaller)
	"""

	process(args)

	logging.basicConfig(format='%(asctime)s - %(name)s [%(levelname)s] %(message)s')
	log = logging.getLogger("Wrapper_freebayes")
	log.setLevel(args.logging_level)
	log.info("Start Wrapper for freebayes")
	log.info("Command: " + " ".join(sys.argv))
	log.debug("DEBUG level message")
	log.info("INFO level message")
	log.warning("WARNING level message")
	log.error("ERROR level message")
	log.critical("CRITICAL level message")
	#command(args, log)
	Error(args, log)
	Warning(args, log)
	#wich(args.variantcaller)
	#freebayes.freeprocess(args)
	#xatlas.xatlasprocess(args)
	#octopus.octoprocess(args)
	octopus.octocommand(args,log)

