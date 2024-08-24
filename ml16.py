#Example-09
import numpy as np
#Are all elements  nonzero
print( np.all( [1,2,3,-4] )    )     #True
print( np.all( [1,2,3,-4,0] )  )     #False

#Is any elements non-zero
print( np.any( [1, 2, 3, 4] )     )          #True
print( np.any( [1, 2, 3, 4, 0] )    )        #True
print( np.any( [0, 0, 0, 0. , 0] )    )      #False
print( np.any( [0, 0, 0, 0. , 0, -1] )   )    #True