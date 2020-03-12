
#my_lambdata/my_mod.py
import pandas

def null_test(xdf):
    isnull = xdf.isnull().sum()
    print("Here is a list of columns and the number of missing values:")
    print(isnull)

import pandas

def add_a_col(l, xdf):
    l = pandas.Series(l)
    print("Converted list to series")
    l = pandas.DataFrame(l)
    print("Converted series to dataframe")
    xdf['new_col'] = l