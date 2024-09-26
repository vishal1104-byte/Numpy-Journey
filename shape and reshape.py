# import numpy as np 
# var = np.array([[1,2,3],[1,2,3]])
# var2 = np.array([1,2,3,4,5], ndmin=4)
# print(var)
# print(var.shape)                       # This is used to know the shape of the array 
# print()
# print(var2.shape)                     # This is the shape function to know the shape of the array means to know how many rows and columns in the array




#                                                      Reshape Function in python 

# import numpy as np
# var = np.array([1,2,3,4,5,6])
# x = var.reshape(2,3)                                  # Here I reshape the one dimentional array into 2dimentional array 
# print(x)



import numpy as np 
var3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,])
print(var3)
print()
x = var3.reshape(2,3,2)                                # Here I reshaped the one dimentional array into 3 dimentional array
print(x)

one = x.reshape(-1)                                    # Here I reshaped the 3dimentionalarray into one dimentional array   \  Flattening the arrays
#                                                        Flattening array means converting a multidimensional array into a 1D array.
print(one)