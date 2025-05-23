#how to create 3d array 
import numpy as np 
list_3d = [
    [
        [10,20,30],
        [50,80,110],
        [150,250,310],
    ],
    [
        [50,100,200],
        [250,350,500],
        [100,200,300],
    ],
    [
        [100,80,150],
        [1100,1180,1150],
        [1200,2280,1150],
    ]
]
#create 3d array from list 
array_3d = np.array(list_3d)
print(array_3d)
#get dimension 
print(array_3d.ndim)
