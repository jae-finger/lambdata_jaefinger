#my_lambdata/my_script.py

import pandas
from my_lambdata.my_mod import order_of_mag

print("Gotta test this out, yo.")

df = pandas.DataFrame({"a" : [0, 1, 2], "b" : [3, 4, 5]})
print(df.head())


x = 10

print(f"Let's increase x ({x}) by an order of magnitude using a custom function called order_of_mag")
print(f"Bam-  the function increased x from {x} to {order_of_mag(x)}")