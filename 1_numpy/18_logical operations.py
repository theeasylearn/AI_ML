import numpy as np 
array1 = np.array([10,20,30,40,50])
array2 = np.array([60,70,80,90,100])

print(array1,array2)
#array1 [False,False,False,True,True]
#array2 [True,True,False,False,False]
result_and = np.logical_and(array1>30,array2<80)
#result_and = [False,False,False,False,False]
print(result_and)


result_or = np.logical_or(array1>30,array2<80)
#result_or = [True,True,False,True,True]
print(result_or)

result_not = np.logical_not(array1>30)
#result_not = [True,True,True,Fals,False]
print(result_not)

result_xor = np.logical_xor(array1>30,array2<80)
#result_xor = [True,True,False,True,True]
print(result_xor)