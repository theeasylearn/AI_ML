# Slide 20: NumPy copy()

- The `copy()` method returns an array copy of the given object.
- Syntax: `numpy.copy(array)`
- **Arguments**:
  - **array**: Input data
- **Returns**: An array copy.
- **Example**:
  ```python
  import numpy as np
  array0 = np.arange(5)
  array1 = np.copy(array0)
  print('Array copied from Array: ', array1)  # [0 1 2 3 4]
  list1 = [1, 2, 3, 4, 5]
  array2 = np.copy(list1)
  print('Array copied from List: ', array2)  # [1 2 3 4 5]
  tuple1 = (1, 2, 3, 4, 5)
  array3 = np.copy(tuple1)
  print('Array copied from Tuple: ', array3)  # [1 2 3 4 5]