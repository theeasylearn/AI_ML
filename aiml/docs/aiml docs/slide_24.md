# Slide 24: Example of Array Attributes

- **Example**:
  ```python
  import numpy as np
  arr = np.array([[1, 2, 3], [4, 5, 6]])
  print("Array: \n", arr)
  print("Dimensions (ndim):", arr.ndim)  # 2
  print("Shape:", arr.shape)  # (2, 3)
  print("Size:", arr.size)  # 6
  print("Data type:", arr.dtype)  # int64
  print("Item size (bytes):", arr.itemsize)  # 8
  print("Total bytes:", arr.nbytes)  # 48
  print("Transpose: \n", arr.T)