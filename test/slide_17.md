# Slide 17: NumPy linspace()

- The `linspace()` method creates an array with **evenly spaced elements** over an interval.
- Syntax: `numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)`
- **Arguments**:
  - **start**: The start value of the sequence (can be array-like)
  - **stop**: The end value of the sequence (can be array-like)
  - **num** (optional): Number of samples to generate (int)
  - **endpoint** (optional): Specifies whether to include end value (bool)
  - **retstep** (optional): If True, returns steps between the samples (bool)
  - **dtype** (optional): Type of output array
  - **axis** (optional): Axis in the result to store the samples (int)
- **Returns**: Array of evenly spaced values.