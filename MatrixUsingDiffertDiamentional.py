from numpy import *
import numpy as numpy

matrixOneWithThreeByTwoDia = numpy.array([[2, 2], [2, 1], [1, 2]])
print matrixOneWithThreeByTwoDia
matrixOneWithTwoByOneDia = numpy.array([[2], [2], [2]])
print matrixOneWithTwoByOneDia
# addition of these two matrix
print (matrixOneWithThreeByTwoDia + matrixOneWithTwoByOneDia)
# /////////////////////////////
print
matrixTwoWithOneByTwoDia = numpy.array([2, 2])
print (matrixOneWithThreeByTwoDia + matrixTwoWithOneByTwoDia)

# multiplication of matrix and matrix
# m1 = numpy.array([[1, 3, 2], [4, 0, 1]])
# print m1
# m2 = numpy.array([[1, 3], [0, 1], [5, 2]])
# print m2
# print (m1 * m2)

# Shape of the matrix
print "Shape Of the matrix"
print matrixOneWithThreeByTwoDia.shape
print "size of an array"
print matrixOneWithThreeByTwoDia.size
print "how to create in single diamentional from multi diamentional"
inSingledia = matrixOneWithThreeByTwoDia.flatten()
print inSingledia
# how to convert matrix in 2 diamentional array
print"how to print matrix in  3 row and 2col"
threeRowAndTwoColumn=inSingledia.reshape(3,2)
print threeRowAndTwoColumn
print"how to print matrix in  2row and 3col"
twoRowAndThreecol=inSingledia.reshape(2,3)
print twoRowAndThreecol



