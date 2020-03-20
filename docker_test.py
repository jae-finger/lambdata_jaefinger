# Run the docker container based on the dockerfile,
# then `python3` to start the python terminal. Enter
# the following lines to demonstrate it working.

import numpy as np
from my_lambdata.my_mod import is_nan

my_list = [4, 3, 2, 0, np.NaN, 2, 4]

is_nan(my_list)
