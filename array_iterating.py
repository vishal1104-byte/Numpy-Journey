'''
Iterating Arrays
Iterating means going through elements one by one.

As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
'''


#          Iterating over 1D array - If we iterate on a 1-D array it will go through each element one by one.
# import numpy as np 
# var = np.array([1,2,3,4,5,6,7])
# for x in var:
#     print(x)


#           Iterating over 2d array - In 2D array it will go through all the rows


# var2 = np.array([[1,2,3],[4,5,6]])
# for y in var2[1]:
#     print(y)


# for a in var2:
#     for b in a:
#         print(b)                       # Iterate on each scalar element of the 2-D array:



#   Iterating 3-D array   |    In a 3-D array it will go through all the 2-D arrays.

# import numpy as np
# var3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# for x in var3:
#     print(x)
#     for y in x:
#         print(y)                             # Iterate the array in 2-D array
#         for z in y:
#             print(z)                                 # iterate on each scalar element of the 3-D array



#                                    Iterating array using nditer()
# The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration

import numpy as np
arr = np.array([[[1,2],[3,4],[5,6],[7,8],[9,10]]])
for x in np.nditer(arr):
    print(x)                                # This is used to iterate on each scalar element of any dimention 