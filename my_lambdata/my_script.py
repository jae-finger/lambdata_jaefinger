# my_lambdata/my_script.py
import numpy as np
import pandas
from my_lambdata.my_mod import is_nan
from my_lambdata.my_mod import add_a_col

#Try out is_nan function
my_list = [4, 3, 2, 0, np.NaN, 2, 4]
is_nan(my_list)

# Check out the add_a_col function
df = pandas.DataFrame(
                    {
                        "a": [0, 1, 2, 3, 4, 5, 6],
                        "b": [3, 4, 5, 6, 7, 8, 9],
                        "y": [100, 10, 100, 5, 0, 50, 10]})
add_a_col(my_list, df)
print(df)
