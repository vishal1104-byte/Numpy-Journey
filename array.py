# Creating the array in numpy 

# import numpy as np
# a = np.array([1,2,3,4,5,6])
# print(a)

# x = [1,2,3,4,5]
# y = np.array(x)
# print(type(y))                                       # To see the data type of a variable



import numpy as np
l = []
for i in range(1,6):
    int_1 = input("Enter:")
    l.append(int_1)
print(np.array(l))                                        # creating array using loops 
