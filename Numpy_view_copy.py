'''
The Difference Between Copy and View

The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
'''


#                                                          COPY

import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42                          # See this is the property of an copy that I change the original array's first index as 42 but it doesnot change the copy that is x
print(arr)
print(x)

y = arr.view()
arr[2] = 11
print(arr)
print(y)                          # See here I change the arr than view is also change because it does not own the data that it is getting affected with original data  


#                                                      checking if arrays owns it data
print(x.base)
print(y.base)