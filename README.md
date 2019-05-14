# Variant-CallerWrapped
Wrapper for Variant-Caller execution

# Goal
Run the desired variant caller and takes as argument the BAM / CRAM, the reference genome  and other options depending on the variant caller 

# Options
  -vc VARIANT_CALLER, --variant_caller VARIANT_CALLER | help: the path to the variantcaller installation folder

  --vc_path VC_PATH | help: the required option when you do not find the path of variantcaller

  -g GENOME_REF, --genome_ref GENOME_REF | help: the reference genome file

  -b BAM, --bam BAM | help: the bam file

  -v VCF, --vcf VCF | help: the output vcf file

  -s SAMPLE, --sample SAMPLE |  help: Sample name to use in the output VCF file

  --slurm | help: Required option when you want to run multiple jobs

  -N NODE, --node NODE | help: the number of nodes used

  -c CORE, --core CORE | help: the number of cores used

  -t THREAD, --thread THREAD | help: the number of threads used

  -be BED, --bed BED | help: the bed file containing target regions

  -l {DEBUG,INFO,WARNING,ERROR}, --logging-level {DEBUG,INFO,WARNING,ERROR} | help: The logger level. [Default: DEBUG]

# status
Development in progress -




