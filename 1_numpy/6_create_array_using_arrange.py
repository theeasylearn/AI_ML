#arrange function in numpy 
import numpy as np 

#create array that has values between 0 to 10 
stop = 10 
array1 = np.arange(10)
print(array1)

#create array that has values between 10 to 100 and step value is 2  
start = 10 
stop = 100
array2 = np.arange(start,stop,step=2)
print(array2)

#create array that has values between 100 to 10 and step value is 2 where type is float
start = 10 
stop = 100
array3 = np.arange(stop,start,step=-2,dtype=float)
print(array3)