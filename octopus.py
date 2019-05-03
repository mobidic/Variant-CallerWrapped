import argparse
import os
import re


#################################wrapper for octopus####################################

def octoprocess(args):
	variantcaller = args.variantcaller
	genomeref = args.genomeref
	bam = args.bam
	output = args.vcf

	print("{} -R {} -I {} -t {}".format(variantcaller, genomeref, bam, output))


def octocommand(args,log):
	variantcaller = args.variantcaller
	genomeref = args.genomeref
	bam = args.bam
	bed = args.bed
	#output = args.prefix

 	log.info("Execute command : {} -R {} - I {} -t {} ".format(variantcaller, genomeref, bam, bed))
	os.system("{} -R {} -I {} -t {} ".format(variantcaller, genomeref, bam, bed))
	#print(cmd)

 	return 0

 	###############################################################################
#
# CLASS
#
################################################################################
"""class LoggerAction(argparse.Action):
    
    @summary: Manages logger level parameters (The value "INFO" becomes logging.info and so on).
    
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
	
	parser.add_argument('-va', '--path', default = "/softs/octopus/bin/octopus", help= 'the path to the freebayes installation folder')
	parser.add_argument('-R', '--genomeref', default = '/usr/local/share/refData/genome/hg19/hg19.fa', help= 'reference genome.fasta')
	parser.add_argument('-I', '--bam', help= 'bam file')
	
	#parser.add_argument('-p', '--prefix', help = 'output prefix')

	parser.add_argument('-t', '--bed', help= ' bed file containing target regions')
	#parser.add_argument('-t', '--thread', help = 'number of threads used', type = int)

	args = parser.parse_args()
	
	if args.thread:
		print(args.thread * 2)

	if args.variantcaller:
		print(args.variantcaller)
	

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
	freecommand(args, log)


	log.info("End Wrapper freebayes annotation")
	#cmd_return = freecommand(args,log)

	octoprocess(args)
	octocommand(args,log)
"""
