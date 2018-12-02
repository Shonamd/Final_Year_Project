import io
import os
import subprocess
import re
from subprocess import Popen, PIPE
import Split, FindVolume, FindBrightness, Rejoin
import matplotlib.pyplot as plt



#Initialise array with volume levels and brightness levels
vol_arr = []
bright_values = []

def find_time(video) :
	#This will call a command that will find the duration of the video
	command_time = "ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 " + video
	#This will call the command using python
	proc=subprocess.Popen(command_time, shell=True, stdout=subprocess.PIPE, )
	#This will return the output of the command (the duration) but will return it as a byte object
	x=proc.communicate()[0]
	print(type(x))
	#This will change the byte object to a string
	a = "".join(map(chr, x))
	print(type(a))
	#This will remove uncessary remains from the byte oject and return the time in seconds as an integer
	x = int(re.search(r'\d+', a).group())
	print(type(x))
	print("Time is  " + str(x))
	return x

def extract_audio(video, x):

	#Add a path to the audio files
	APP_ROOT = os.path.dirname(os.path.abspath(__file__))

	target = os.path.join(APP_ROOT, 'audio/')

	if not os.path.isdir(target):
		os.mkdir(target)

	audio_command = "ffmpeg -i " + video +" -vn "+ target +"/audio_output_"+str(x)+".wav"
	subprocess.call(audio_command,shell=True)
	vol = FindVolume.find_volume(target+'/audio_output_'+str(x)+'.wav')
	vol_arr.append(vol)

def split_video(video) :

	#Add the path of the uploaded video
	APP_ROOT = os.path.dirname(os.path.abspath(__file__))

	target = os.path.join(APP_ROOT, 'visual/')

	if not os.path.isdir(target):
		os.mkdir(target)


	i = 0 

	time = find_time(video)

	num_seg = int(time/10)

	for x in range(0, num_seg-1) :

		command = "ffmpeg -i " + video + " -vcodec copy -acodec copy -ss " +  str(i) +  " -t 00:00:10 " + target + "/video_output_" + str(x) +".mp4"
		subprocess.call(command,shell=True)
		

		extract_audio('visual/video_output_'+str(x)+'.mp4', x)
		Split.GetFrames('visual/video_output_'+str(x)+'.mp4', x)
		i = i + 10
		#print(i)

	bright_values = list(FindBrightness.find_brightness())


	plt.plot(vol_arr)
	plt.plot(bright_values)
	plt.legend(["Volume level", "Brightness level"], loc='upper left')
	plt.ylabel("Brightness level")
	plt.xlabel("10 second increments")
	plt.show()

	#Rejoin clips

	Rejoin.Rejoin(vol_arr, bright_values)
	
	#Clear elements from array
	vol_arr.clear()
	bright_values.clear()

#find_time('output.mp4')
#split_video('test.mp4')
#print(vol_arr)