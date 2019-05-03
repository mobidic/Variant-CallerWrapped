
#!/usr/bin/env python
# encoding: utf-8

import argparse
import os
import re


#################################wrapper for xatlas####################################



def xatlascommand(args, log):
	variantcaller= args.variantcaller
	genomeref = args.genomeref
	bam = args.bam

	bed = args.bed
	sample = args.sample
	output = args.prefix

	log.info("Execute command : {} -r {} -i {}  -c {} -s {} -p".format(variantcaller, genomeref, bam, bed, sample,output))
 	os.system("{} -r {}  -i {}  -c {} -s {} -p {}".format(variantcaller, genomeref, bam, bed, sample, output))
 	log.debug("the -s argument is required")

 	

 	return 0

 	###xatlas =/usr/local/bin/xatlas


