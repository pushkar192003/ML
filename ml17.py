#Example-10

#Types of Operation Broadcasting:-
# 1) Scaler Operation Broadcasting
# 2) Array Operation Broadcasting
import numpy as np

n1 = np.array([4,5,6])
n2 = np.array([1,2,3])

print( "n1   =   " , n1     )   #[4,5,6]
                               #   +
print( "n2   =   " , n2     )   #[1,2,3]
print( "n1 + n2 = ", n1 + n2  )
print( "n1 - n2 = ", n1 - n2  )

n3 = np.array([4,5,6,7])
print( n1+ n3 )
#NOTE:
# Shape must be the same for array operation broadcasting