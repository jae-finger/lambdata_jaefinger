
#my_lambdata/my_mod.py
import pandas

def null_test(xdf):
    isnull = xdf.isnull().sum()
    print("Here is a list of columns and the number of missing values:")
    print(isnull)

def add_col_to_df(l, xdf):
    #Add's list l by converting to dataframe then adds to xdf
    l = pandas.Series(l)
    return l
