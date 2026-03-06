# working through python for data science from freeCodeCamp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# define a 1 dimensional array like this:
a = np.array([1,2,3,4,5,6,7])
b = np.array([1,3,5,6,7,3,4])
#print(a)
#print(b)
# concatenate arrays like this
c = np.array([a, b])
#print(c)

# multi dimensional arrays. This array is a 4x3 2D array
d = np.array([[1,2,3], [4,5,6], [6,7,8], [1,2,4]])

#print(d)
#print(e)

# copying arrays and taking parts of them
# f is a variable that points to the part of the array after index
# 3 of array a while g is its own array
f = a[3:]
#print(f)
g = b[2:5].copy()
#print(g)

# special types of matrixes/ndarrays
A = np.ones((2,2)) # special n x m only made out of ones
B = np.eye(2,2) # n x n identity matrix
C = np.zeros((2,2)) # matrix of zeros
D = np.diag((6,7)) # matrix that makes the diagonal the input
E = np.block([[A,B], [C,D]]) # makes a block of homogenous elemements

# creates an array 0-11 and then arranges them into a 2x6 matrix
h = np.arange(12)
i = h.reshape(2,6)
#print(i)

# creates 9 random numbers between 0 and 1 and rearranges them into a 3x3
j = np.random.rand(9)
k = j.reshape(3,3)
#print(k)

# generates 10 mil random numbers and arranges them into a histogram visualized with plt
l = np.random.randn(10000000)
plt.hist(l,bins=200)
# 2x4x3 matrix of random integers between 5 and 15
m = np.random.randint(5,15, size=(2,4,3))
# print(m)

# creates a random permutation of 0-99 and reshapes them to a 5x20 matrix
n = np.random.permutation(100).reshape(5,20)
#print(n)

##### SLICING #####

# A[start:end:step]
a = np.arange(10)

a1 = a[1:5] # index 1 till 5 but not 5 -> 1,2,3,4
#print(a1)
a2 = a[:5] # index 0 stil 5 but not 5 -> 0,1,2,3,4
#print(a2)

a3 = a[2:] # index 2 to the end -> 2,3,4,5,6,7,8,9 
#print(a3)

a4 = a[::-1] # from end to start (reverse the array)
#print(a4)

# All the a{x} variables are pointers accessing the og a memory not copies


# Accessing single rows in a ndim array
X = np.random.randint(20, size=(5,5))
#print(X)

#print("The second row of X is: " , X[2])
#print("the third index of the second row is: " , X[2,3])

# transpose of the matrix
#print(X.T)

X.sort(axis = 0)
print(X)
