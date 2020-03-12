#my_lambdata/my_script.py

import pandas
from my_lambdata.my_mod import null_test

df = pandas.DataFrame({"a" : [0, 1, 2, 3, 4, 5, 6,], "b" : [3, 4, 5, 6, 7, 8, 9], "y" : [100, 10, 100, 5, 0, 50, 10]})

null_test(df)


from my_lambdata.my_mod import add_a_col

l = [4, 3, 2, 1, 0, 1, 2]
l = add_a_col(l)
print(l)