# how to copy array 
import numpy as np 
list = [10,5,18,9,25,7]
tuples = (45,30,90,75,65)

#create an array from list 
array1 = np.copy(list)

#create an array from tuple
array2 = np.copy(tuples)

array3 = np.arange(0,100,step=4)

#create array from array 
array4 = np.copy(array3)

print(array1,array2,array3,array4)
