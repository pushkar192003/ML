#Example-08
import numpy as np
arr = np.array( [11, 22, -33,  0,  44, 55] )
#                0    1   2    3    4   5
print( "arr.sum() = " , arr.sum()  )  #This is member function
print( np.sum(arr) )      #This is univarasal function
print( "arr.std() = " , arr.std()  )
print( "arr.mean()   = ", arr.mean() )
print( "np.mean(arr) = ", np.mean(arr) )
print( "arr.max() = " , arr.max()  )
print( "arr.min() = " , arr.min()  )
print( "arr.size = "  , arr.size   )
print( "arr.shape ="  , arr.shape  )
print( "arr.dtype= "  , arr.dtype  )
# following line will print( index of nonzero values )
print( "arr.nonzero() = ", arr.nonzero() )