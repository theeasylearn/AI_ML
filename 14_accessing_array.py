import numpy as np 
#create 1d array
arr = np.array([10,20,30,40,50])
print(arr)
#display 1st value 
print(arr[0]) # 10
#display 1st 3 value 
print(arr[0:3]) # 10 20 30 

#change first value 
arr[0] = 100
print(arr)

#change 2nd 3rd and 4th value 
arr[1:4] = [200,300,400]
print(arr)

#conditional change
#change only that value which is less then 100 
arr[arr<100] = 99 
print(arr)

arr_2d = np.array([
    [100,200,300],
    [400,600,800],
])

print(arr_2d)
#single value change
arr_2d[0,0] = 999
print(arr_2d)

#change multiple values 
# Rows: 0:2 → Select rows 0 and 1 (i.e., the first two rows).
# Columns: 0:2 → Select column 0 and 1 (i.e., the first two column).
arr_2d[0:2,0:2] = 555 #here 0:2 1st value in [] represent row's range to be selected and another 0:2 2nd value in bracket represent column range
print(arr_2d)