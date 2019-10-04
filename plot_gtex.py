import data_viz
import argparse
import os

def linear_search(key, L):
    for index in range(len(L)):
        if key == L[index]:
            return index
    return -1

def binary_search(key, L):
    low = -1
    high = len(L)

    while high - low > 1:
        mid = (high + low) // 2

        if key == L[mid]:
            return mid

        elif key > L[mid]:
            low = mid
        else:
            high = mid
    return -1


def main():
    LINEAR_OR_BINARY = 0
    parser = argparse.ArgumentParser(
            description='Program that outputs a boxplot of the expression' + \
                        ' of a gene from either tissue groups or tissue types.',
            prog='geneexpressionplotter')

    parser.add_argument('--gene_reads',
                        type=str,
                        help='The file with the readings of each gene.',
                        required=True)

    parser.add_argument('--sample_attributes',
                        type=str,
                        help='The file with the attribes of each sample.',
                        required=True)

    parser.add_argument('--gene',
                        type=str,
                        help='The gene selected.',
                        required=True)

    parser.add_argument('--group_type',
                        type=str,
                        help='Either SMTS or SMTSD.',
                        required=True)

    parser.add_argument('--output_file',
                        type=str,
                        help='The filename of the output plot.',
                        required=True)

    args = parser.parse_args()

    gene_reads = args.gene_reads
    sample_attributes = args.sample_attributes
    gene = args.gene
    group_type = args.group_type
    output_file = args.output_file

    if not os.path.exists(gene_reads) or not os.path.exists(sample_attributes):
        print('Gene readings or sample attributes file does not exist or could not be read, quitting.')
        quit(1)

    if group_type != "SMTS" and group_type != "SMTSD":
        print('Group type is either SMTS or SMTSD, quitting.')
        quit(1)



if __name__ == '__main__':
    main()
