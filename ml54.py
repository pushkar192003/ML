#Filling null value with the next ones
#------------------------------------------

import pandas as pd
import numpy as np

# dictionary of lists
dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]
       }

# creating a dataframe from dictionary
df = pd.DataFrame(dict)

# filling  null value using fillna() function
df2 = df.fillna(method='bfill')

print( df )
print( df2 )