# A powerful N-dimensional array object
# NumPy can also be used as multidiamensional container as generic data

from numpy import *
import numpy as numpy
from array import *

array = numpy.array([[1,2,3],[1,2,3]])
print "print multidiamensional array==="
print array
print
print "Type of array"
print (type(array))
print
print " n Diamension of an array (No of row in array)=="
print (array.ndim)
print
print "Shape of an array="
print (array.shape)
print
print "size of an array="
print (array.size)
print
print "data type of an array="
print (array.dtype)

