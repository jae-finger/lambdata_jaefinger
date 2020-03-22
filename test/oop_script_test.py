#test/my_mod_test.py

import unittest
import numpy as np
from my_lambdata.oop_refactored_script import NullFinder

class nullfinder_test(unittest.TestCase):
    def test_isnan(self):
        test_list_na = [1, np.NaN]
        nullf_na = NullFinder(test_list_na)
        nulls = nullf_na.findnulls()
        self.assertEqual(nulls[1], "Yes") #Green Light
        self.assertNotEqual(nulls[1], "No") #Red Light

if __name__ == '__main__':
    unittest.main()