
#my_lambdata/my_mod.py


def null_test(xlist):
    isnull = xlist.isnull().sum()
    print("Here is a list of columns and the number of missing values:")
    print(isnull)