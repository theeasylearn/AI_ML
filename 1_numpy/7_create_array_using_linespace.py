#create array using linespace 
import numpy as np 

#create array using linespace that has 10 value between 0 and 1 (including)
array1 = np.linspace(0.0,1.0,10)
print(array1)

#create array using linespace that has 10 value between 10 and 100  (including) of int type
array2 = np.linspace(10,100,10,dtype=int)
print(array2)

#create array using linespace that has 10 value between 10 and 100  (excluding) of int type
array3 = np.linspace(10,100,10,endpoint=False,dtype=int)
print(array3)