# my_lambdata/my_mod.py
import pandas


def null_test(xdf):
    """
    This is a function that returns the number of missing values for each
    column in a dataframe.

    Input: xdf = a pandas DataFrame
    Outputs: Prints a list containing a row corresponding to each column and
    the number of missing values in each column of the dataframe.
    """
    isnull = xdf.isnull().sum()
    print("Here is a list of columns and the number of missing values:")
    print(isnull)


def add_a_col(m, xdf):
    """
    This is a function that converts list m to a series, then to a dataframe,
    and adds that column to an existing dataframe xdf.

    Input: m - a list of values to be added as a column to a dataframe
    Input: xdf - a dataframe to which the column will be added
    """
    l = pandas.Series(m)
    print("Converted list to series")
    l = pandas.DataFrame(m)
    print("Converted series to dataframe")
    xdf['new_col'] = m
