#                                   Arrays Filled with zeros     ||  0s

import numpy as np
ar_zero = np.zeros(4)  # Arrays filled with zeros     0s
ar_zero2 = np.zeros((2,3))          # Arrays filled with zeros on 2 dimentional array
ar_zero3 = np.zeros(((3,4)))        # Arrays Filled with zeros on 3 dimentional array
print(ar_zero)   
print(ar_zero2)   
print(ar_zero3)   

#                                   Arrays filled with ones       ||    1s

ar_ones = np.ones(4)  # Arrays filled with ones     0s
ar_ones2 = np.ones((2,3))          # Arrays filled with ones on 2 dimentional array
ar_ones3 = np.ones(((3,4)))        # Arrays Filled with ones on 3 dimentional array
print(ar_ones)   
print(ar_ones2)   
print(ar_ones3) 



#                                  Range of array using --->   arange function 

ar_rn = np.arange(5)
print(ar_rn)



#                                  Diagonal Array using ------> eye function    Give output as an binary format

ar_dia = np.eye(3)
print(ar_dia)