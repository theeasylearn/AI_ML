## Slide 28: Important Functions in Random Module

| Function                          | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| `rand()`                          | Uniform distribution over [0,1). Accepts shape as positional arguments.      |
| `randn()`                         | Standard normal distribution (mean=0, std=1). For normally distributed data. |
| `randint(low, high, size)`        | Random integers from low (inclusive) to high (exclusive).                    |
| `random()`                        | Random floats in [0.0, 1.0). Similar to `rand()` but shape passed as a tuple. |
| `choice()`                        | Randomly selects elements from a given array.                               |
| `shuffle()`                       | Randomly shuffles elements in a one-dimensional array in place.    