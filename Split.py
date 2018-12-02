import cv2
import math
import os


def GetFrames(video, iteration):

	#Add a path to the frames 
	APP_ROOT = os.path.dirname(os.path.abspath(__file__))

	#Create folders to hold the frames for each 10 second clip
	target = os.path.join(APP_ROOT, 'frames/')
	it_target = os.path.join(APP_ROOT, 'frames/' + str(iteration))

	if not os.path.isdir(target):
		os.mkdir(target)

	if not os.path.isdir(it_target):
		os.mkdir(it_target)


	#Use the file
	vid = cv2.VideoCapture(video)
	#Get the frame rate of the video
	frame_rate = vid.get(cv2.CAP_PROP_FPS)
	#While the video is running
	while(vid.isOpened()):
		#Will get the index of the frame to be captured next
		frame_count = vid.get(1)
		#Will read tuple of boolean( can file be acessed) and image
		sucess, image = vid.read()

		#If video is over will break loop
		if(sucess != True):
			break

		#If the frame count mod the frame rate is 0 then it will save the current frame
		if(frame_count % math.floor(frame_rate) == 0):
			filename =   str(int(frame_count)) + ".jpg"
			cv2.imwrite(it_target+'/'+filename, image)

