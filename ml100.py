'''reading a csv file using csv reader and converting into array'''
'''def mode read'''
import csv
file = open('IMdB_India_Top250.csv')
f_name = csv.reader(file)
'''def delimitter is comma while reading '''

'''converts into 2D array'''
array=list(f_name)
print(array)
'''prints number of rows '''
print(len(array))

