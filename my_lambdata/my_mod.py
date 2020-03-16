# my_lambdata/my_mod.py
import pandas
import numpy as np


def is_nan(m):
    """
    This is a function that returns whether a number in a list is NaN

    Input: m = a list of numbers or NaNs
    Outputs: Prints a list of whether each element is a number (yes) or NaN (no).
    """
    is_null = []
    for x in m:
        if x is np.NaN:
            is_null.append('Yes')
        else:
            is_null.append('No')
    print("A list of each elements and yes it is a number or no it isn't:")
    print(is_null)


def add_a_col(m, xdf):
    """
    This is a function that converts list m to a series, then to a dataframe,
    and adds that column to an existing dataframe xdf.

    Input: m - a list of values to be added as a column to a dataframe
    Input: xdf - a dataframe to which the column will be added
    """
    m = pandas.Series(m)
    print("Converted list to series")
    m = pandas.DataFrame(m)
    print("Converted series to dataframe")
    xdf['new_col'] = m
