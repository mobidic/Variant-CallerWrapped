#!/usr/bin/env python
# encoding: utf-8

import argparse
import os
import re
import logging # logging messages
import sys


#################################wrapper for freebayes####################################

def freecommand(args, log):

	variantcaller = args.variantcaller
	genomeref = args.genomeref
	bam = args.bam

	bed = args.bed
	output = args.prefix
	
	log.info("Execute command : {} -f {} -t {} {} -v {}".format(variantcaller, genomeref, bed, bam, output))
	os.system("{} -f {} -t {} {} -v {}".format(variantcaller, genomeref, bed ,bam, output))

	return 0


	###path =/usr/local/bin/freebayes

 