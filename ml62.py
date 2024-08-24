# Create a DataFrame object from list of tuples with columns and indices.
df = pd.DataFrame(players,  columns=['Name', 'Age', 'Place', 'Sex'],
                            index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k'])

print("Original Dataframe = \n", df)


# show the boolean dataframe
print(" \nshow the boolean Dataframe : \n\n", df.isnull())

report = df.isnull().sum()
# Count total NaN at each column in a DataFrame
print(" \nCount total NaN at each column in a DataFrame : \n\n", report )


print("df.info() = \n" )
df.info()