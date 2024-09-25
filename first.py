# To see which is faster numpy or list we can do the following thing 

# %timeit [j**4 for j in range(1,9)]           # Note you can check this in jupiter notebook 



# import numpy as np 
# name = []
# for i in range(1,6):
#     print("Enter the name of the students who want to take participate in the competition:")
#     a = input("Enter: \n")
#     name.append(a)

# print(name)


import numpy as np
a = np.array([1,2,3,4,5])                               # To check the dimension of the array 
print(a.ndim)