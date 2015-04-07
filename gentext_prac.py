#!/usr/bin/env python
import numpy as np
import pickle
import csv

'''
read in 4 column data, first row is data names
this reads in line by line so our data (which was in columns)
is all jumbled up
'''
raw_data = np.genfromtxt("tab_data.tsv", dtype=tuple)

#taking the transpose will let me sort my data sets
data = raw_data.T

print data.shape()

'''
the .tolist() function I just learned about today, it casts a numpy array
to a standard python list. sometimes it is usefull to use vanilla python
'''
data = data.tolist()

'''
split my data into meaningful arrays, remember each element in data is
an entire column (would be rows but we were smart and transposed that biatch).
'''

a = data[0]
b = data[1]
c = data[2]
d = data[3]

#turn this back into a tsv for practice!
with open("new_tabs.tsv", "w") as f:
	writer = csv.writer(f, delimiter='\t') #\t is the tab space deliminater
	writer.writerows(zip(a,b,c,d))

#the same method can be used to write csv's
with open("new_csv.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerows(zip(a,b,c,d))

'''
Let's store this into a dictionary (much easier to use later). also remember
that the first elements in a, b, c and d are the titles or names of each column of data
since we know this we can easily split off our titles and actual data sets in the dictionary
'''
new_data = {a[0]:a[1:], b[0]:b[1:], c[0]:c[1:], d[0]:d[1:]}

#just an example of how to call data out of a python dictionary 
new_a = new_data['a']
new_b = new_data['b']
new_c = new_data['c']
new_d = new_data['d']

#dictionaries can be saved as pickle files and used easily for later use
pickle.dump(new_data, open("pickle_tab.p", "wb"))

#how to load a pickle. upload is going to be a dictionary which is an exact copy of new_data
upload = pickle.load(open("pickle_tab.p", "rb"))

