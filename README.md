# parallel-arrays-profiling-and-benchmarking
Parallel Arrays, Profiling, and Benchmarking

# Description

The Python script `plot_gtex.py` allows one to create a plot of boxplots of the expressions for a chosen gene through either tissue groups or tissue samples. The script was written for two specifi datesets, one containing the gene readings, and the other containing the attributes of the samples. Both may be accessed through the following links.
- https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
- https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

# Usage

The basic usage of `plot_gtex.py` is as follows.

```
geneexpressionplotter [-h] --gene_reads GENE_READS --sample_attributes SAMPLE_ATTRIBUTES --gene GENE --group_type GROUP_TYPE --output_file OUTPUT_FILE
```

Where gene_reads is the file containing the gene readings, sample_attributes is the file containing the attributes of the samples, gene is the target gene, group type is to choose to go by tissue types(SMTS) or tissue groups(SMTSD), and output_file is the filename of the output plot.

# Installation

Installation is done through Conda, to install Conda enter the following commands

```
cd $HOME
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b
. $HOME/miniconda3/etc/profile.d/conda.sh
conda update --yes conda
conda config --add channels bioconda
echo ". $HOME/miniconda3/etc/profile.d/conda.sh" >> $HOME/.bashrc
```

We then create a new environment and install the supported python version. Here we simply name the Conda environment `pgtenv`.

```
conda create --yes -n pgtenv
conda install --yes python=3.6
```

Finally we go into this environment, install the needed package, `matplotlib`, and pull the repository.

```
conda activate swe4s
conda install -y matplotlib
git clone https://github.com/cu-swe4s-fall-2019/best-practices-f-collins.git
```

The files this script was designed for may again be accessed at the following links:
- https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
- https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

# Profiling and Benchmarking Results

There was a very noticeable difference between the speed of the program using the linear_search function versus the binary_search function. When calling the linear_search function, it in total took a bit under 11 seconds to run, with the calls to linear_search taking up about 9 seconds of that total time. When we used the binary_search function where we could, the total time dropped to less than 2 seconds, with the binary search function taking 0.057 seconds of that time, and the remaining calls to linear_search taking 0.026. Clearly, it is important to know which parts of a program take the longest time to compute, and to focus on those when optimizing.
