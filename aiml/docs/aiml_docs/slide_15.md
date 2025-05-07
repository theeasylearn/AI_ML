# Slide 15: NumPy ones()

- The `ones()` method creates a new array of given shape and type, filled with **ones**.
- Syntax: `numpy.ones(shape, dtype=None, order='C')`
- **Arguments**:
  - **shape**: Desired new shape of the array (can be integer or tuple of integers)
  - **dtype** (optional): Datatype of the returned array
  - **order** (optional): Specifies the order in which the ones are filled
- **Returns**: Array of given shape, order, and datatype filled with ones.
- **Example**:
  ```python
  import numpy as np
  array1 = np.ones(5)
  print('Float Array: ', array1)  # Output: [1. 1. 1. 1. 1.]