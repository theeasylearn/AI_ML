#array attributes 
import numpy as np 
batches = [
    [5,10,20,25], # MERN stack
    [10,20,30,40], # flutter
    [5,20,40,80], # other batches
] 
#convert it into array
array1 = np.array(batches)
print(array1)
print("Dimension in array",array1.ndim)
print("Total values in array",array1.size)
print("Rows and columns in array",array1.shape)
print("each item size in array",array1.itemsize)
print("total bytes of array in memory ",array1.nbytes)
print("type of array ",array1.dtype)