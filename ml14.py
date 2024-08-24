import numpy as np
#We can create numpy array from range
ar = np.arange(11,16)  # Rule of II & EE
print( "ar = " , ar )
#ar = [11, 12, 13, 14, 15]
#      0   1    2   3   4
ar[3] = 77

print( "After updating, ar = " , ar )
#[11, 12, 13, 77, 15]