#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    import numpy as np
    cleaned_data = []

    ### your code goes here
    len_ = len(ages)
    error = [None] * len_
    for i in range(len_):
        error[i] =  predictions[i] - net_worths[i]
    large_value_index = sorted(range(len(error)), key=lambda i: error[i])[-9:]
    print large_value_index
    for i in reversed(range(len_)):
        if (i in large_value_index):
            del error[i]
            ages = np.delete(ages, i)
            net_worths = np.delete(net_worths, i)
    print "size of ages: " , len(ages)
    cleaned_data = zip(ages, net_worths, error)
    return cleaned_data
