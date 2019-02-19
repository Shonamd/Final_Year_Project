import cv2
import numpy as np
from matplotlib import image as image

def getImage(src):
	image = cv2.imread(src)

	return image

def displayThresh(original, binary):
	displayImage = cv2.bitwise_and(original,original,mask=binary)
	return displayImage

def dilate(mask, kernel):
	newMask = cv2.dilate(mask, kernel)
	return newMask

def erode(mask, kernel):
	newMask = cv2.erode(mask, kernel)
	return newMask

def show(image):
	cv2.imshow("", image)
	key = cv2.waitKey(0)

def getWhite(image):
	whiteImage = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2YUV)
	RangeLower = (100,110,100)
	RangeUpper = (255,130,200)

	B = cv2.inRange(whiteImage, RangeLower, RangeUpper)

	return B

def getYellow(image):
	yellowImage = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2HSV)
	RangeLower = (20, 100, 100)
	RangeUpper = (30, 255, 255)

	B = cv2.inRange(yellowImage, RangeLower, RangeUpper)

	return B

def getRed(image):
	redImage = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2HSV)

	RangeLower = cv2.inRange(redImage, (0,100,100), (5,180,180))
	RangeUpper = cv2.inRange(redImage, (175,100,100), (180,180,180))

	B = RangeLower + RangeUpper

	return B

def getBlue(image):
	blueImage = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2HSV)

	RangeLower = (110, 50, 50) 
	RangeUpper = (130, 255, 255)

	B = cv2.inRange(blueImage, RangeLower, RangeUpper)
	return B

def getBlankImage(image):
	blankImage = image.copy()
	blankImage[:, :] = (0,0,0)

	return blankImage

def binaryThresh(image):
	G = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(G,1,255,cv2.THRESH_BINARY)

	return thresh

def getContours(image):
	contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	# im2, contours, hierarchy = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	return contours

def filterContourByShapefootball(image, contours, byWidth):
	tempBlank = getBlankImage(image.copy())

	for i in range(len(contours)):
		x,y,w,h = cv2.boundingRect(contours[i])
		# area = cv2.contourArea(contours[i])
		# cv2.fillPoly(tempBlank, pts =[contours[i]], color=(255,255,255))
		if (h < w  ):
			cv2.fillPoly(tempBlank, pts =[contours[i]], color=(255,255,255))
			object_detect = True

	contourBinary = binaryThresh(tempBlank)

	# react_area = w*h
	# extent = float(area)/react_area
	# print(extent)

	return contourBinary, object_detect

def filterContourByShapegolf(image, contours, byWidth):
	tempBlank = getBlankImage(image.copy())

	for i in range(len(contours)):
		x,y,w,h = cv2.boundingRect(contours[i])
		#cv2.fillPoly(tempBlank, pts =[contours[i]], color=(255,255,255))
		if (h > w ):
			cv2.fillPoly(tempBlank, pts =[contours[i]], color=(255,255,255))
			object_detect = True

		print(" height is  " + str(h))
		print("width is " + str(w))
	contourBinary = binaryThresh(tempBlank)


	return contourBinary, object_detect

def goal_detect(src):

	object_detect = False
	
	#src = "goaltest2.jpg"

	original = getImage(src)

	whiteMask = getWhite(original.copy())

	#whiteMask = boundaryDetect(whiteMask)

	#Check the display
	whiteDisplay = displayThresh(original, whiteMask)

	show(whiteDisplay)

	#Step 2 - Calculate the contours
	whiteContours = getContours(whiteMask)

	#print(whiteContours)

	whiteFiltered, object_detect = filterContourByShapefootball(original, whiteContours, True)

	show(whiteFiltered)

	#print(whiteFiltered)
	#print(len(whiteFiltered))

	kernel = np.ones((75,75), np.uint8)

	whiteEroded = erode(whiteFiltered, kernel)
	whiteDilated = dilate(whiteEroded , kernel)

	show(whiteDilated)

	#print(object_detect)
	return(object_detect)
	#area = cv2.contourArea(whiteDilated)

	#print(area)

def flag_detect(src):
	
	#src = "golf1.jpg"

	object_detect = False
		
	original = getImage(src)

	#show(original)

	yellowMask = getYellow(original.copy())

		#whiteMask = boundaryDetect(whiteMask)

		#Check the display
	yellowDisplay = displayThresh(original, yellowMask)

	#show(yellowDisplay)

		#Step 2 - Calculate the contours
	yellowContours = getContours(yellowMask)

	yellowFiltered, object_detect = filterContourByShapegolf(original, yellowContours, True)

	#show(yellowFiltered)

	#print(object_detect)

	# kernel = np.ones((75,75), np.uint8)

	# whiteEroded = erode(whiteFiltered, kernel)
	# whiteDilated = dilate(whiteEroded , kernel)
	return(object_detect)

	# show(whiteDilated)



#flag_detect('flag.jpg')