# Slide 10: Array

- Use `np.array()` to convert a list to a **NumPy array**, which is a powerful data structure for numerical computing.
- **Creates Arrays from Lists or Tuples**:
  - Converts Python lists, tuples, or other sequences into a NumPy array, enabling efficient numerical operations.
- **Supports Multi-Dimensional Arrays**:
  - Creates 1D, 2D (matrices), or higher-dimensional arrays for complex data.
- **Automatically converts elements** to a common data type for consistency.
- **Code Example**:
  ```python
  import numpy as np
  arr = np.array([1, 2, 3])  # create 1D array
  print(arr)  # Output: [1 2 3]
  b = np.array([1, 2, 3, 4.5])
  print(b)  # Output: [1. 2. 3. 4.5]