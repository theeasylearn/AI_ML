# Slide 14: NumPy zeros()

- The `zeros()` method creates a new array of given shape and type, filled with **zeros**.
- Syntax: `numpy.zeros(shape, dtype=None, order='C')`
- **Arguments**:
  - **shape**: Desired shape of the new array (can be int or tuple of int)
  - **dtype** (optional): Datatype of the new array
  - **order** (optional): Specifies the order in which the zeros are filled
- **Returns**: Array of given shape, order, and datatype filled with zeros.
- **Example**:
  ```python
  import numpy as np
  array1 = np.zeros(5)
  print(array1)  # Output: [0. 0. 0. 0. 0.]