#2)Checking for missing values using not null()

#In order to check null values in Pandas Dataframe, we use notnull() function
#This function return dataframe of Boolean values which are False for NaN values.

import pandas as pd
import numpy as np

# dictionary of lists
dict = {'First Score' : [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score' : [np.nan, 40, 80, 98]
       }

# creating a dataframe using dictionary
df = pd.DataFrame(dict)

# using notnull() function
bool_df2 = df.notnull()

print("\n\n", df   )
print("\n\n", bool_df2   )
