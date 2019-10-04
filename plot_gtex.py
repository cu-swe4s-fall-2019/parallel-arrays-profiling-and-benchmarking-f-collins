import data_viz
import argparse
import os
import csv
import gzip

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

        if key == L[mid][0]:
            return L[mid][1]

        elif key > L[mid][0]:
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

    sa_file = csv.reader(open("GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt", "r"), delimiter = "\t")                       
    gr_file = csv.reader(gzip.open("GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz", "rt"), delimiter = "\t")
    
    sa_header = []
    sampids = []
    tissues = []
    for row in sa_file:
        if sa_header == []:
            sa_header = row
            i = 0
            for entry in sa_header:
                if entry == "SAMPID":
                    sampidcol = i
                elif entry == group_type:
                    groupcol = i
                i += 1
            continue
        sampids.append(row[sampidcol])
        tissues.append(row[groupcol])

    gr_header = []
    dimension = []
    samplenames = []
    samplevals = []
    genenamecol = 0
    for row in gr_file:
        if row[0][0] == "#":
            continue
        if dimension == []:
            dimension = row
            continue
        if gr_header == []:
            i = 0
            gr_header = row
            genenamecol = gr_header.index("Description")
            for sample in gr_header[(genenamecol + 1):]:
                if LINEAR_OR_BINARY == 0:
                    samplenames.append(sample)
                if LINEAR_OR_BINARY == 1:
                    samplenames.append([sample, i])
                    i += 1
            if LINEAR_OR_BINARY == 1:
                samplenames.sort(key=lambda tup: tup[0])

        if row[genenamecol] == gene:
            for expression in row[(genenamecol + 1):]:
                samplevals.append(expression)


    if samplevals == []:
        print('Gene not found in gene readings, quitting.')
        quit(1)

    samplelocations = []
    locationdata = []
    iteminlist = 0
    index = 0
    for sampleid, tissue in zip(sampids, tissues):
        if linear_search(tissue, samplelocations) == -1:
            samplelocations.append(tissue)
            locationdata.append([])

        if LINEAR_OR_BINARY == 0:
            geneexpressindex = linear_search(sampleid, samplenames)
        if LINEAR_OR_BINARY == 1:
            geneexpressindex = binary_search(sampleid, samplenames)

        if geneexpressindex != -1:
            locationdata[linear_search(tissue, samplelocations)].append(int(samplevals[geneexpressindex]))

    data_viz.boxplot(locationdata, output_file, gene, samplelocations, group_type, "Gene read counts")


if __name__ == '__main__':
    main()
