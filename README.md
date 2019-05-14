# Variant-CallerWrapped
Wrapper for Variant-Caller execution
# Goal
Run the desired variant caller and takes as argument the BAM / CRAM, the reference genome  and other options depending on the variant caller 
# Options
-h, --help            show this help message and exit
  -vc VARIANT_CALLER, --variant_caller VARIANT_CALLER
                        the path to the variantcaller installation folder
  --vc_path VC_PATH     the required option when you do not find the path of
                        variantcaller
  -g GENOME_REF, --genome_ref GENOME_REF
                        the reference genome file
  -b BAM, --bam BAM     the bam file
  -v VCF, --vcf VCF     the output vcf file
  -s SAMPLE, --sample SAMPLE
                        Sample name to use in the output VCF file
  --slurm
  -N NODE, --node NODE  the number of nodes used
  -c CORE, --core CORE  the number of cores used
  -t THREAD, --thread THREAD
                        the number of threads used
  -be BED, --bed BED    the bed file containing target regions
  -l {DEBUG,INFO,WARNING,ERROR}, --logging-level {DEBUG,INFO,WARNING,ERROR}
                        The logger level. [Default: DEBUG]
#status
Development in progress -




