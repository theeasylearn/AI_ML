import numpy as np 

#create two array 
x = np.array([10,20,30,40,50])
y = np.array([10,60,30,80,50])

print(x)
print(y)

#compare array element by element 
result1 = x == y 
result2 = x != y 

print(result1)
print(result2)

#all function to get both array are exactly same or not 
print(np.all(result1))

#any function to get if any one element match in array or not
print(np.any(result2))