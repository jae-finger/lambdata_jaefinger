# Refactored script code with OOP approach

import pandas as pd
import numpy as np


class NullFinder():
    def __init__(self, num_list):
        self.num_list = num_list

    def findnulls(self):
        is_null = []
        for x in self.num_list:
            if x is np.NaN:
                is_null.append('Yes')
            else:
                is_null.append('No')
        print(is_null)


test_list = [4, 3, 2, 0, np.NaN, 2, 4]
nullf = NullFinder(test_list)

nullf.findnulls()
