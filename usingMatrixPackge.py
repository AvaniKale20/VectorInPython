from operator import __mul__

from numpy import *
import numpy as numpy

print "this matrix using numpy -----"
arr1 = array([[2, 3, 2], [1, 2, 3]])
print arr1
print
# we have to convert this 2d array in matrix , there is function called as matrix
print "this matrix is converted into matrix using matrix function-----------"
m = matrix(arr1)
print m
print
m2 = matrix(arr1)
result = m + (m2)
print "sum of two matrix---", result
print

# Second way to use matrix  function
print
print "Second way to use matrix  function------"
m_without_using_Array = matrix('2 3 2 ; 1 2 3')
print m_without_using_Array
print

# multiplication of matrix
print "multiplication of matrix---"
m_one = numpy.matrix('1 2 3 ; 1 2 3')
m_two = numpy.matrix('1 2 3 ; 1 2 3')
MULTI = m_one * m_two
print MULTI
