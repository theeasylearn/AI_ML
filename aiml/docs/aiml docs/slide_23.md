# Slide 23: Array Attributes

| **Attribute**       | **Description**                                                                 | **Example Output**                     |
|---------------------|--------------------------------------------------------------------------------|----------------------------------------|
| `ndarray.ndim`      | Number of dimensions (axes)                                                    | 2 for a 2D array                       |
| `ndarray.shape`     | Tuple representing the size of each dimension                                  | (3, 4) for 3 rows, 4 columns           |
| `ndarray.size`      | Total number of elements in the array                                          | 12 for a 3×4 array                     |
| `ndarray.dtype`     | Data type of the array elements                                                | int32, float64, etc.                   |
| `ndarray.itemsize`  | Size (in bytes) of each element                                                | 4 bytes for int32                      |
| `ndarray.nbytes`    | Total memory (in bytes) consumed by the array                                  | 48 for 12 elements × 4 bytes           |
| `ndarray.T`         | Transposed array (rows become columns and vice versa)                          | Flips axes                             |