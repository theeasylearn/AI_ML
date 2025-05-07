# Slide 18: Example of linspace() Function

- **Example**:
  ```python
  import numpy as np
  array1 = np.linspace(2.0, 3.0, num=5)
  print(array1)  # Output: [2.   2.25 2.5  2.75 3.  ]
  array2 = np.linspace(2.0, 3.0, num=5, endpoint=False)
  print("Array2: ", array2)  # Output: [2.  2.2 2.4 2.6 2.8]
  array3, step_size = np.linspace(2.0, 3.0, num=5, retstep=True)
  print("Array3: ", array3)  # Output: [2.   2.25 2.5  2.75 3.  ]
  print("Step Size: ", step_size)  # Output: 0.25