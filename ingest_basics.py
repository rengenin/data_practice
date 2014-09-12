import numpy as np

'''Just a reminder to my self on basic data ingestion (VERY BASIC)'''

'''ingesting text based data'''
#White space separated variables
ssv = np.array([float(f) for f in file('space_del_data.txt').read().split()])
#Comma separated
csv = np.array([float(f) for f in file('csv_data.txt').read().split(",")])
#Cleaner ^ reads in line by line
data = [line.strip() for line in open('data.lst')]


'''ingesting wav file'''
from scipy.io.wavfile import read
wav_file = read('test.wav')

#Break out different data parts
sampling_rate = wav_file[0]
wav_array = wav_file[1]
