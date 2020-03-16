import pandas as pd
import numpy as np 

class NullFinder():
    def __init__(self, num_list):
        self.num_list = num_list
    
    def findnulls(parameter_list):
        is_null = []
        for x in my_list_with_null:
            if x is np.NaN:
                is_null.append('Yes')
            else:
                is_null.append('No')


# my_list_with_null = [1, 2, np.NaN]
# my_list_withouta_null = [3, 4, 5]
# is_null = []
# for x in my_list_with_null:
#     if x is np.NaN:
#         is_null.append('Yes')
#     else:
#         is_null.append('No')
# print(is_null)
# is_null = []
# for x in my_list_withouta_null:
#     if x is np.NaN:
#         is_null.append('Yes')
#     else:
#         is_null.append('No')

# print(is_null)