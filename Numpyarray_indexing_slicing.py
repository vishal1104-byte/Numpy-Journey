#                                                             NUPPY ARRAYS INDEXING
'''
Access Array Elements
Array indexing is the same as accessing an array element.

You can access an array element by referring to its index number.

The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.
'''



# import numpy as np
# var = np.array([1,2,3,4,5,6])
# print(var[0:2])                                         # This is the indexing to access the 1D array

# var2 = np.array([[1,2,3,4],[1,2,3,4]])
# print(var2[0,3])                                     # To access the 2D array  |     o is the for full array bracket and 3 is for accesing the access from the list 




# var3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(var3[0,2,2])                                    # To access the 3D array           \   0 is the main array in which all the three arrays are stored , 2 is the array which is group with 2 more arrays    and  2 is the elements of the the array which is accessed as 2 



# #                                           Negative Indexing 
# varn = np.array([[1,2,3,4,5], [6,7,8,9,0]])
# print(varn[1, -1])                                      # To do negative indexing to access the element using negative value




#                                                      NUMPY ARRAYS SLICING 

'''Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].'''


#                                                 Slicing 1D array 

import numpy as np
arr = np.array([1,2,3,4,5,6])
print([arr[1:5]])                                    # Slicing the array from index 1 to index 5   \   Note: It include the starting index but exclude the last index which is 5 

arrn = np.array([1,2,3,4,5])
print(arrn[-1])


#                                                  Slicing 2D array 
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(arr2[1,1:3])                                   # It will return the element from index 1 to 3 from the subindex 1 which is  second array 
print(arr2[0:2,3])                                   # It will return 3 index from both the array
print(arr2[0:2,0:4])                                 # It will return the element of index 1 to 4 from both the array 