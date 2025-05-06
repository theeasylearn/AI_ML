import numpy as np 

# create 1d array using ones function of float type
size = 10
array1 = np.ones(size)
print('float array',array1)


#create 1d array using one function of integer type 
array2 = np.ones(size,dtype=int)
print('int array',array2)

#create 2d array using one function of integer type 
rows = 3
column = 5
dimension = (rows,column)
array3 = np.ones(dimension,dtype=int)
print('2d array(nd array) int array',array3)
