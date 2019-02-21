import numpy as np
import os
import cv2
from matplotlib import image as image

def findImageChange():

	folder_num = 0

	bright_arr = []
	bright_folder = []

	change_arr = []
	path = 'frames'

	#Find the number of folders availible
	for path, dirs, files in os.walk(path):
		folder_num += len(dirs)

	for i in range(0, folder_num):
		change_arr.append(findChange('frames/'+str(i)+'/0.jpg', 'frames/'+str(i)+'/9.jpg')[0])

	return(change_arr)


standard_thresh = .5

def getImage(src):
	image = cv2.imread(src)
	return image

def show(image):
	cv2.imshow("", image)
	key = cv2.waitKey(0)

def mapDist(frame1, frame2):
	#Outputs the pythagoran distance between two frames
	frame1_32 = np.float32(frame1)
	#print(frame1_32)
	frame2_32 = np.float32(frame2)
	#print(frame2_32)
	distance = cv2.absdiff(frame1, frame2)
	#diff32 = frame1_32 - frame2_32
	#print(diff32)
	#norm32 = np.sqrt(diff32[:,:,0]**2 + diff32[:,:,1]**2 + diff32[:,:,2]**2)/np.sqrt(255**2 + 255**2 + 255**2)
	#distance =np.uint8(norm32*255)
	return distance

def findChange(frame1, frame2):

	src1 = frame1
	src2 = frame2

	frame1 = getImage(src1)
	frame2 = getImage(src2)

	# show(frame1)
	# show(frame2)


	#cv2.imshow('distance', frame2)
	distance = mapDist(frame1, frame2)

	#print(distance)
	# frame1 = frame2
	# frame2 = frame3

	# apply gausian smoothing
	mod = cv2.GaussianBlur(distance, (5, 5), 0)

	#apply thresholding
	_, thresh = cv2.threshold(mod, 100, 255, 0)

	#Calculate the standard of deviation
	_, standard_of_dev = cv2.meanStdDev(mod)

	#print(standard_of_dev)

	standard_of_dev = standard_of_dev.flatten()

	#print(standard_of_dev)

	cv2.imshow('distance', mod)

	return(standard_of_dev)
	# if standard_of_dev[0] > standard_thresh:
	# 	print("Motion was detected")

	# else:
	# 	print("Try another photo")

#https://software.intel.com/en-us/node/754940
#print(findImageChange())
