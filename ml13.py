#np.zeros and np.ones to generate prefiled matrix with 0 and 1 respectively
#by default datatype is float we can provide additional parameter along with dimensions ,dtype=ourchoice
#using operation broadcasting
import numpy as np

zr = np.zeros( [ 3,4] )
print( "Zero filed array zr = \n" , zr  )

ar = np.ones([4,4], dtype=int )   #By default is float
print( "1's filed array ones = \n" , ar  )

print( ar * 4  )
print( ar.dtype )



zr2 = np.zeros( [2,5] )
print( "Zero filed array zr2 = \n", zr2 )



zr = np.zeros( [2, 3, 4] )
print( "Zero filed array zr = \n" , zr  )
print("Total no of values = ", zr.size )
print("zr.shape = ", zr.shape )
print("zr.ndim   = ", zr.ndim  )