import numpy as np

arr = np.random.rand(4)                               # for generating the random numbers between 0 and 1 
print(arr) 

r2 = np.random.randn(4)                               # This will generate a random value close to zero This may return positive or negative numbers as well
print(r2)

r3 = np.random.ranf(4)                                # The function for doing random sampling in numpy 
print(r3)

r4 = np.random.randint(1,5,5)                          # This function is used to genarate a random number be in a range 
print(r4)