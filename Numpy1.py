import numpy as np

print('arrange and reshape function:')
a=np.arange(1,16,2).reshape(2,4)
print(a)        # prints 1D as array 1 upto 15 differ by 2 if we couldn't use reshape() function.
# Reshape() argument's product must be equal to the number of elements present in the array.

print('shape function:')
print(a.shape)


print('dtype function::')
print(a.dtype)

print('itemsize::')     # size of datatype
print(a.itemsize)

print('size:')          # how many numbers a matrix have
print(a.size)


