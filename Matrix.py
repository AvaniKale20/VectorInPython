from numpy import *
import numpy as numpy

matrixOne = numpy.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print matrixOne
print
print ("size of matrix", matrixOne.size)

print
# Addition of matrix
matrixTwo = numpy.array([[1, 2], [1, 2]])
print ("matrix two with 2*2 diamentional")
print matrixTwo

matrixThree = numpy.array([[1, 2], [1, 2]])

print ("matrix three with 2*2 diamenstional")
print matrixThree
print ("addition of both matrix=")
print matrixTwo + matrixThree
print

# Multiplication of matrix
print ("multiplication of matrix=")
print matrixThree * matrixTwo

# Divide operation on matrix
print ("divide operation on matrix")
print matrixThree/matrixTwo


