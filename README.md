# lambdata_jaefinger

## Installation
You can install `lambdata_jaefinger` using the following code:
```python
pip install -i https://test.pypi.org/simple/ lambdata-jaefinger
```

## Usage
There are two helper functions available:
1. `is_nan()` :
Returns whether each element is a number (yes) or not (no).
```python
from my_lambdata.my_mod import is_nan
my_list = [4, 3, 2, 0, np.NaN, 2, 4]
is_nan(my_list)
```

2. `add_a_col()`:
Converts a list to a series then adds it to an existing dataframe.
```python
from my_lambdata.my_mod import add_a_col
df = pandas.DataFrame(
    {
        "a": [0, 1, 2, 3, 4, 5, 6],
        "b": [3, 4, 5, 6, 7, 8, 9],
        "y": [100, 10, 100, 5, 0, 50, 10]})
add_a_col(my_list, df)
print(df)
```