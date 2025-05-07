# Slide 16: NumPy arange()

- The `arange()` method creates an array with **evenly spaced elements** as per the interval.
- Syntax: `numpy.arange(start=0, stop, step=1, dtype=None)`
- **Arguments**:
  - **start** (optional): The start value of the interval range (int or real)
  - **stop**: The end value of the interval range (exclusive) (int or real)
  - **step** (optional): Step size of the interval (int or real)
  - **dtype** (optional): Type of output array
- **Examples**:
  ```python
  import numpy as np
  array1 = np.arange(5)  # [0 1 2 3 4]
  array2 = np.arange(5, 10)  # [5 6 7 8 9]
  array3 = np.arange(5, 15, 2)  # [5 7 9 11 13]
  print(array1, array2, array3)