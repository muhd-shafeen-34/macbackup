import numpy
matrix1 = numpy.matrix([[1,2,3],[4,5,6],[7,8,9]])
matrix2 = numpy.matrix([[9,8,7],[6,5,4],[3,2,1]])
addition = numpy.add(matrix1,matrix2)
subtraction = numpy.subtract(matrix1,matrix2)
multiply = numpy.matmul(matrix1,matrix2)
scalar = 2*matrix1
transpose = numpy.transpose(matrix1)
print(matrix1)
print("addition of two matrices:\n",addition)
print("\nsubtraction of two matrices:\n",subtraction)
print("\nmultiplication of two matrices:\n",multiply)
print("\nscalar multiplication of matrix 1:\n",scalar)
print("\nTranspose of matrix 1:\n",transpose)

