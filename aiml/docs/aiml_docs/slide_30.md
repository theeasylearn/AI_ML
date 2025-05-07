## Slide 30: Creating Complex Numbers in NumPy

- Use `numpy.array()` to create an array of complex numbers.
- Define numbers with `j` to indicate the imaginary part.

```python
import numpy as np

# Creating a complex number array
complex_num = np.array([3+4j, 1-2j])
print("Complex Array:", complex_num)

# Checking the data type
print("Data Type:", complex_num.dtype)
```