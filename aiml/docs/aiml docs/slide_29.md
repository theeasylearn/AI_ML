## Slide 29: Example of Functions in Random Module

```python
import numpy as np
np.random.seed(42)  # Ensures reproducibility
print(np.random.rand(2, 2))  # 2 × 2 array of random floats
print(np.random.randint(1, 10, 5))  # 5 random integers from 1 to 9
print(np.random.normal(0, 1, 3))  # 3 values from normal distribution
print(np.random.choice([1, 2, 3]))  # Randomly picks one element
arr = np.array([10, 20, 30, 40, 50])  # Define array
np.random.shuffle(arr)  # Shuffles array in-place
print(arr)
```