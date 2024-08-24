import numpy as np
na = np.array( [  [1,  2, 3,np.nan],
                  [4,  5, 6,7] ]  )

print( "na = \n" , na )
print( "na.transpose() = \n", na.transpose() )
print( "na = \n" , na )

print(  "np.eye = \n", np.eye(3)  )    # To create square matrix
