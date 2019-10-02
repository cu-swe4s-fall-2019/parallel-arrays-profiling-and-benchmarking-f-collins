import matplotlib as mpl
import matplotlib.pyplot as plt
import math_lib as ml


mpl.use('agg')

"""A number of functions that output various visualizations of input data.
"""
def boxplot(L, out_file_name):
    '''Creates a boxplot of the input data.

    Parameters:
        L: A list containing the input data
        out_file_name: The filename to save the file as.
    '''
    if out_file_name is None:
        return None

    fig = plt.figure(figsize=(5, 5), dpi=300)

    ax = fig.add_subplot(1, 1, 1)
    ax.boxplot(L)

    fig.suptitle("mean: " + str(ml.list_mean(L)) + " stddev: " +
                 str(ml.list_stdev(L)))

    plt.savefig(out_file_name, bbox_inches='tight')


def histogram(L, out_file_name):
    '''Creates a histogram of the input data.

    Parameters:
        L: A list containing the input data
        out_file_name: The filename to save the file as.
    '''
    if out_file_name is None:
        return None

    fig = plt.figure(figsize=(5, 5), dpi=300)

    ax = fig.add_subplot(1, 1, 1)
    ax.hist(L, bins=10)

    fig.suptitle("mean: " + str(ml.list_mean(L)) + " stddev: " +
                 str(ml.list_stdev(L)))

    plt.savefig(out_file_name, bbox_inches='tight')


def combo(L, out_file_name):
    '''Creates a combination of a boxplot and a histogram of the input data.

    Parameters:
        L: A list containing the input data
        out_file_name: The filename to save the file as.
    '''
    if out_file_name is None:
        return None

    fig = plt.figure(figsize=(8, 5), dpi=300)

    ax = fig.add_subplot(1, 2, 1)
    ax.boxplot(L)

    ax = fig.add_subplot(1, 2, 2)
    ax.hist(L, bins=10)

    fig.suptitle("mean: " + str(ml.list_mean(L)) + " stddev: " +
                 str(ml.list_stdev(L)))

    plt.savefig(out_file_name, bbox_inches='tight')
