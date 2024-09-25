# 1 Dimensional array

import numpy as np 
array = np.array([1,2,3,45])
print(array.ndim)


# 2 Dimentional array

array2 = np.array([[1,2,3,4],[1,2,3,4]])
print(array2)
print(array2.ndim)

# 3 Dimentional array
array3 = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]],[[1,2,3,4],[1,2,3,4],[1,2,3,4]],[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(array3)
print(array3.ndim)

arrn = np.array([1,2,3,4] , ndmin=10)              # This is used to make the multidimentional arrays and ndmin function is used to set the number of dimention in array 
print(arrn)
print(arrn.ndim)