from array import *
from numpy import *
import numpy as np
class Vector:

    print "Addition Operation"
    # Vector Row
    vector_rows=np.array([1,2,3])
    print vector_rows
    print
    # Vector column
    vector_column=np.array([[1],
                           [2],
                           [3]])
    print (vector_column)

    print
    # Addition of two vector row
    vector_row_one=np.array([1,2,3])
    vector_row_two=np.array([1,2,3])
    print ("addition of two vector row =")
    print (vector_row_one+vector_row_two)

    print
    # Addition of two vector column
    vector_column_one = np.array([[1],
                                  [2],
                                  [3]])
    vector_column_two = np.array([[1],
                                  [2],
                                  [3]])
    print ("addition of two vector row =")
    print vector_column_one + vector_column_two
    print

    # Addition of one vector column and one row vector
    vector_row_three = np.array([1,2,3])
    vector_column_four = np.array([[10],
                                  [15]])
    print ("addition of 1*3 one vector row and 2*1 one vector column =")
    print vector_row_three + vector_column_four
    print

    # Addition of 3*1 one vector column and 3*1 one column vector
    vector_row_five = np.array([1, 2, 3])
    vector_column_six = np.array([[10],
                                   [15],
                                   [10]])
    print ("addition of 1*3 one vector row and 3*1 one vector column =")
    print vector_row_five + vector_column_six
    print
    # ---------------------------------------------------------------------------------------------
    print "Multiplication Operation"
    # Multiplication of one vector column and one row vector
    vector_row_seven = np.array([1, 2, 3])
    vector_column_seven = np.array([[10],
                                   [15]])
    print ("Multiplication of 1*3 one vector row and 2*1 one vector column =")
    print vector_row_three * vector_column_four
    print
    # ---------------------------------------------------------------------------------------------
    print "Subtraction Operation"
    # Subtraction between two row vector
    vectorOneRowForSubtraction = np.array([3,3,4])
    vectorTwoRowForSubtraction = np.array([1,2,1])
    print ("Subtraction of 1*3 vectorOneRowForSubtraction and  vectorTwoRowForSubtraction =")
    print vectorOneRowForSubtraction - vectorTwoRowForSubtraction
    print

    # Subtraction between One row vector and one column vector
    vectorOneRowForSubtraction = np.array([3, 3])
    vectorTwoColumnForSubtraction = np.array([[1],
                                           [2]])
    print ("Subtraction between vectorOneRowForSubtraction & vectorTwoColumnForSubtraction  =")
    print vectorOneRowForSubtraction - vectorTwoColumnForSubtraction
    print
    # ---------------------------------------------------------------------------------------------

    print "Divide Operation"
    # Dividation between two row vector
    vectorOneRowForDivide = np.array([3,3,4])
    vectorTwoRowForDivide = np.array([3,3,2])
    print ("Divide operation on  1*3 vectorOneRowForDivide and  vectorTwoRowForDivide =")
    print vectorOneRowForDivide / vectorTwoRowForDivide
    print


   

