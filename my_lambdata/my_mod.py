
#my_lambdata/my_mod.py


def null_test(xlist):
    isnull = xlist.isnull().sum()
    print("Here is a list of columns and the number of missing values:")
    print(isnull)

import pandas

def add_a_col(l, df):
    l = pandas.Series(l)
    print("Converted list to series")
    l = pandas.DataFrame(l)
    print("Converted series to dataframe")
    df = pandas.