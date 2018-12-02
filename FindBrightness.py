#Convert image to greyscale and return mean 
from PIL import Image, ImageStat
import cv2
import numpy
import os

def find_brightness():

	folder_num = 0

	bright_arr = []
	bright_folder = []

	path = 'frames'

	#Find the number of folders availible
	for path, dirs, files in os.walk(path):
		folder_num += len(dirs)

		#Go through each folder and find the brightness and add to an array
	for i in range(folder_num):
		for file in os.listdir('frames/' + str(i)):
			bright_arr.append(brightness('frames/' + str(i) + '/' + file))

		#Find the highest level of brightness and normalise to a level around 1 - 100
		bright_level = max(bright_arr)
		bright_level = bright_level/10*4
		bright_folder.append(bright_level)
		bright_arr = []

	return(bright_folder)


#Find the brightness
def brightness( frame ):
	#Convert the image to greyscale
	im = Image.open(frame).convert('L')
	#Find the number on the greyscale
	stat = ImageStat.Stat(im)
	#return the average level of brightness
	return stat.mean[0]