import numpy as np
import scipy
import scipy.io.wavfile as wavfile
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt
import sys

def find_volume(video):

	#Find the data and rate
	fs_rate, signal = wavfile.read(video)

	#Use fourier transformation to find the amplitude of the signal
	signal_fft = np.fft.fft(signal)

	#Split the file into chunks
	segments = np.array_split(abs(signal_fft), 20)

	#Apply the formula to compute the volume
	dbs = [20*np.log10(np.sqrt(np.mean(segment**2))) for segment in segments]

	return np.mean(dbs)