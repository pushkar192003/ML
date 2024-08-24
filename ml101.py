import numpy

f_name= open('indians-diabetes.data.csv')

array=numpy.loadtxt(f_name,delimiter=',')
print(array.shape)
