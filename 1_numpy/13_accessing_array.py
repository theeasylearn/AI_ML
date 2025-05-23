import numpy as np 
list_2d = [
    [10,20,30],
    [40,50,60],
    [70,80,90],
]

#convert it into array 
array_2d = np.array(list_2d)

#1st row 2nd column 
print(array_2d[0,1]) # 20
print(array_2d[2,2]) # 90

#get 2nd column value 
print(array_2d[:,1]) #[20 50 80]

#get 2nd row 
print(array_2d[1,:]) #[40 50 60]

print(array_2d[0:3,0:2]) #[40 50 60]

#filter value (value above 40)
print(array_2d[array_2d>40]) 

#filter value (value below 50)
print(array_2d[array_2d<50]) 