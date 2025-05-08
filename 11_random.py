import numpy.random as rd 
import numpy as np 

#create 2d array using random 
arr_2d = rd.rand(3,3)
print(arr_2d)

#create 1d integer array
arr_1d = rd.randint(10,100,10)
print(arr_1d)

arr_normal = rd.normal(10,100,10)
print(arr_normal)

rd.shuffle(arr_1d)
print(arr_1d)