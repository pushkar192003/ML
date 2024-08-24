#Display only those rows which are having Gender = NULL.

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_column', None)
pd.set_option('display.width', 1000)
# making data frame from csv file
data = pd.read_csv("employees_with_missing_data.csv")

# creating bool series True for NaN values
#bool_series = pd.isnull(data["Gender"])
bool_series = data["Gender"].isnull()
print(bool_series)



# filtering data
# displaying data only with Gender = NaN
result = data[bool_series]
print(result)
print(result.shape)
print(result.info() )


# creating bool series True for valid values
#bool_series = pd.isnull(data["Gender"])
bool_series = data["Gender"].notnull()
print(bool_series)



# filtering data
# displaying data only with Gender valid
result = data[bool_series]
print(result)
print(result.shape)
print(result.info() )