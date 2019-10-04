test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest


run gene_files_dont_exist python3 plot_gtex.py --gene_reads dontexist.csv --sample_attributes alsodontexist.csv --gene SDHB --group_type SMTS --output_file a.png
assert_in_stdout 'Gene readings or sample attributes file does not exist or could not be read, quitting.'
assert_exit_code 1

run gene_doesnt_exist python3 plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene BADGENE --group_type SMTS --output_file a.png
assert_in_stdout 'Gene not found in gene readings, quitting.'
assert_exit_code 1

run wrong_gene_group python3 plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene SDHB --group_type BADGROUP --output_file a.png
assert_in_stdout 'Group type is either SMTS or SMTSD, quitting.'
assert_exit_code 1
